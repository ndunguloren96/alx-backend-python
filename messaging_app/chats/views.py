from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Conversation, Message
from .serializers import UserSerializer, ConversationSerializer, MessageSerializer
from django.shortcuts import get_object_or_404


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class ConversationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows conversations to be viewed or edited.
    """
    queryset = Conversation.objects.all().order_by('-created_at')
    serializer_class = ConversationSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned conversations to only those
        where the requesting user is a participant.
        """
        if self.request.user.is_authenticated:
            # Show conversations where the current user is a participant
            return Conversation.objects.filter(participants=self.request.user).order_by('-created_at')
        return Conversation.objects.none() # Or all if authentication is not mandatory

    def perform_create(self, serializer):
        """
        When creating a conversation, ensure the requesting user is added as a participant.
        """
        # Ensure the creating user is part of the participants.
        # If participants are sent in the request, they will be handled by the serializer's create method.
        # This just ensures the creator is included.
        participants = self.request.data.get('participants', [])
        if self.request.user.is_authenticated and str(self.request.user.user_id) not in participants:
            participants.append(str(self.request.user.user_id))
            # Validate that all participants exist
            valid_participants = []
            for uid in participants:
                try:
                    user = User.objects.get(user_id=uid)
                    valid_participants.append(user)
                except User.DoesNotExist:
                    return Response({"detail": f"Participant with ID {uid} does not exist."}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save(participants=valid_participants)
        else:
            serializer.save()

    @action(detail=True, methods=['post'])
    def send_message(self, request, pk=None):
        """
        Custom action to send a message to a specific conversation.
        """
        conversation = get_object_or_404(Conversation, pk=pk)

        # Check if the requesting user is a participant in the conversation
        if not request.user.is_authenticated or request.user not in conversation.participants.all():
            return Response({"detail": "You are not a participant in this conversation."},
                            status=status.HTTP_403_FORBIDDEN)

        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            # Automatically set sender and conversation
            serializer.save(sender=request.user, conversation=conversation)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or created.
    """
    queryset = Message.objects.all().order_by('sent_at')
    serializer_class = MessageSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned messages to those in conversations
        the requesting user is part of.
        """
        if self.request.user.is_authenticated:
            # Get conversations the user is a participant of
            user_conversations = Conversation.objects.filter(participants=self.request.user)
            # Filter messages by those conversations
            return Message.objects.filter(conversation__in=user_conversations).order_by('sent_at')
        return Message.objects.none()

    def perform_create(self, serializer):
        """
        When creating a message, set the sender to the requesting user.
        Also, ensure the user is part of the target conversation.
        """
        conversation_id = self.request.data.get('conversation')
        try:
            conversation = Conversation.objects.get(conversation_id=conversation_id)
        except Conversation.DoesNotExist:
            raise serializers.ValidationError({"conversation": "Conversation not found."})

        if self.request.user.is_authenticated and self.request.user not in conversation.participants.all():
             raise serializers.ValidationError({"detail": "You are not a participant in this conversation."})

        serializer.save(sender=self.request.user, conversation=conversation)

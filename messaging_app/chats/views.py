from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend # Import for filtering

from .models import Conversation, Message, User
from .serializers import ConversationSerializer, MessageSerializer, UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed.
    """
    queryset = User.objects.all().order_by('email')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['email', 'role', 'is_staff', 'is_active']


class ConversationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows conversations to be viewed or edited.
    Users can create new conversations and retrieve their own conversations.
    """
    queryset = Conversation.objects.all().order_by('-created_at')
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['participants', 'created_at']

    def get_queryset(self):
        """
        Ensure users only see conversations they are a part of.
        Superusers can see all conversations.
        """
        user = self.request.user
        if user.is_superuser:
            return Conversation.objects.all()
        return Conversation.objects.filter(participants=user).order_by('-created_at')

    def perform_create(self, serializer):
        """
        When creating a conversation, ensure the current user is a participant.
        """
        # Get participants from validated data
        participants = serializer.validated_data.get('participants')
        
        # Ensure the creating user is always part of the conversation
        if self.request.user not in participants:
            participants.append(self.request.user) # Add current user if not already in list
        
        # Save the conversation with the participants
        serializer.save(participants=participants)


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed, created, or edited.
    Messages are nested under conversations.
    """
    queryset = Message.objects.all().order_by('sent_at')
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sender', 'conversation', 'sent_at']

    def get_queryset(self):
        """
        Ensure messages are filtered by the conversation they belong to,
        and that the requesting user is a participant of that conversation.
        """
        user = self.request.user
        conversation_id = self.kwargs.get('parent_lookup_conversation') # From NestedRouter
        
        if conversation_id:
            conversation = get_object_or_404(Conversation, conversation_id=conversation_id)
            # Ensure the user is a participant of this conversation
            if not user.is_superuser and user not in conversation.participants.all():
                raise status.HTTP_403_FORBIDDEN("You are not a participant of this conversation.")
            return Message.objects.filter(conversation=conversation).order_by('sent_at')
        
        # If no conversation_id is provided, only allow superusers to see all messages
        # or filter for messages sent/received by the current user.
        if user.is_superuser:
            return Message.objects.all()
        
        # For non-superusers without a conversation ID, they can only see messages they sent/received
        # (This implies a message belongs to a conversation they are part of).
        # More precise filtering might be needed depending on exact requirements.
        return Message.objects.filter(models.Q(sender=user) | models.Q(conversation__participants=user)).distinct().order_by('sent_at')


    def perform_create(self, serializer):
        """
        When creating a message, set the sender to the current user
        and associate it with the correct conversation.
        """
        conversation_id = self.kwargs.get('parent_lookup_conversation')
        conversation = get_object_or_404(Conversation, conversation_id=conversation_id)

        # Ensure the sender is the current authenticated user and a participant
        if self.request.user not in conversation.participants.all():
            raise status.HTTP_403_FORBIDDEN("You cannot send messages to a conversation you are not a participant of.")
        
        serializer.save(sender=self.request.user, conversation=conversation)

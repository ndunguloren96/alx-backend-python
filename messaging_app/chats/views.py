# messaging_app/chats/views.py

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from .models import Conversation, Message, User
from .serializers import ConversationSerializer, MessageSerializer, UserSerializer
from .permissions import IsParticipantOfConversation, IsSenderOrReadOnly
from .pagination import MessagePagination # Import custom pagination
from .filters import MessageFilter, ConversationFilter # Import custom filters


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed.
    """
    queryset = User.objects.all().order_by('email')
    serializer_class = UserSerializer
    permission_classes = [] # Global IsAuthenticated from settings will apply
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['email', 'role', 'is_staff', 'is_active']


class ConversationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows conversations to be viewed or edited.
    Users can create new conversations and retrieve their own conversations.
    """
    queryset = Conversation.objects.all().order_by('-created_at')
    serializer_class = ConversationSerializer
    permission_classes = [IsParticipantOfConversation]
    filter_backends = [DjangoFilterBackend]
    # Use the custom filter class instead of filterset_fields for more complex filtering
    filterset_class = ConversationFilter # Apply ConversationFilter


    def get_queryset(self):
        """
        Ensure users only see conversations they are a part of.
        The IsParticipantOfConversation handles object-level permissions for retrieve/update/delete.
        For list action, we still filter the queryset.
        """
        user = self.request.user
        if user.is_superuser:
            return Conversation.objects.all()
        return Conversation.objects.filter(participants=user).order_by('-created_at')

    def perform_create(self, serializer):
        """
        When creating a conversation, ensure the current user is a participant.
        """
        participants = serializer.validated_data.get('participants', [])
        if self.request.user not in participants:
            participants.append(self.request.user)
        serializer.save(participants=participants)


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed, created, or edited.
    Messages are nested under conversations.
    """
    queryset = Message.objects.all().order_by('sent_at')
    serializer_class = MessageSerializer
    permission_classes = [IsParticipantOfConversation, IsSenderOrReadOnly]
    pagination_class = MessagePagination # Apply custom pagination
    filter_backends = [DjangoFilterBackend]
    # Use the custom filter class instead of filterset_fields for time range filtering
    filterset_class = MessageFilter # Apply MessageFilter


    def get_queryset(self):
        """
        Ensure messages are filtered by the conversation they belong to,
        and that the requesting user is a participant of that conversation.
        """
        user = self.request.user
        conversation_id = self.kwargs.get('parent_lookup_conversation')

        if conversation_id:
            conversation = get_object_or_404(Conversation, conversation_id=conversation_id)
            # The IsParticipantOfConversation permission will handle whether the user can access this conversation.
            return Message.objects.filter(conversation=conversation).order_by('sent_at')

        if user.is_superuser:
            return Message.objects.all()
        return Message.objects.filter(conversation__participants=user).distinct().order_by('sent_at')


    def perform_create(self, serializer):
        """
        When creating a message, set the sender to the current user
        and associate it with the correct conversation.
        """
        conversation_id = self.kwargs.get('parent_lookup_conversation')
        conversation = get_object_or_404(Conversation, conversation_id=conversation_id)
        serializer.save(sender=self.request.user, conversation=conversation)

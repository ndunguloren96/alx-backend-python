# messaging_app/chats/views.py

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated # Remove or comment this out
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from .models import Conversation, Message, User
from .serializers import ConversationSerializer, MessageSerializer, UserSerializer
from .permissions import IsParticipantOfConversation, IsSenderOrReadOnly # Import custom permissions


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed.
    """
    queryset = User.objects.all().order_by('email')
    serializer_class = UserSerializer
    # IsAuthenticated is sufficient here, as only viewing users is generally allowed for authenticated users.
    # The global default IsAuthenticated from settings.py will handle this.
    permission_classes = [] # Leave empty or remove if handled globally, otherwise keep IsAuthenticated
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['email', 'role', 'is_staff', 'is_active']


class ConversationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows conversations to be viewed or edited.
    Users can create new conversations and retrieve their own conversations.
    """
    queryset = Conversation.objects.all().order_by('-created_at')
    serializer_class = ConversationSerializer
    # Apply custom permission:
    permission_classes = [IsParticipantOfConversation] # Apply the new custom permission
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['participants', 'created_at']

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
        # Ensure the creating user is always part of the conversation
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
    # Apply multiple custom permissions:
    permission_classes = [IsParticipantOfConversation, IsSenderOrReadOnly] # Apply both permissions
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sender', 'conversation', 'sent_at']

    def get_queryset(self):
        """
        Ensure messages are filtered by the conversation they belong to,
        and that the requesting user is a participant of that conversation.
        The permission class now handles the object-level access check.
        """
        user = self.request.user
        conversation_id = self.kwargs.get('parent_lookup_conversation')

        if conversation_id:
            conversation = get_object_or_404(Conversation, conversation_id=conversation_id)
            # The IsParticipantOfConversation permission will handle whether the user can access this conversation.
            return Message.objects.filter(conversation=conversation).order_by('sent_at')

        # If no conversation_id is provided (e.g., /api/messages/ if it were a top-level view),
        # only allow superusers to see all messages, or filter for messages relevant to the current user.
        # Given the nested router, this block might only be hit by superusers if direct /messages access is enabled.
        if user.is_superuser:
            return Message.objects.all()
        # For non-superusers without a conversation ID, default to messages in their conversations.
        return Message.objects.filter(conversation__participants=user).distinct().order_by('sent_at')


    def perform_create(self, serializer):
        """
        When creating a message, set the sender to the current user
        and associate it with the correct conversation.
        The permission class handles the participant check.
        """
        conversation_id = self.kwargs.get('parent_lookup_conversation')
        conversation = get_object_or_404(Conversation, conversation_id=conversation_id)

        # The IsParticipantOfConversation permission's has_permission already checks
        # if the user can access this conversation. No explicit check needed here.
        serializer.save(sender=self.request.user, conversation=conversation)

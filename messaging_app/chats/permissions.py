# messaging_app/chats/permissions.py

from rest_framework import permissions
from django.shortcuts import get_object_or_404
from .models import Conversation

class IsParticipantOfConversation(permissions.BasePermission):
    """
    Custom permission to only allow participants of a conversation to access it.
    Superusers always have access.
    """

    message = "You are not a participant of this conversation or do not have permission to access it."

    def has_permission(self, request, view):
        """
        Check if the user is authenticated for any action.
        This covers "Allow only authenticated users to access the api"
        """
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """
        Check if the user is a participant of the conversation (for Conversation model)
        or related conversation (for Message model).
        """
        # Allow superusers full access
        if request.user.is_superuser:
            return True

        # For Conversation objects directly
        if isinstance(obj, Conversation):
            return obj.participants.filter(user_id=request.user.user_id).exists()

        # For Message objects (check if the user is a participant of the message's conversation)
        if hasattr(obj, 'conversation') and isinstance(obj.conversation, Conversation):
            return obj.conversation.participants.filter(user_id=request.user.user_id).exists()

        # Fallback for other objects, or if logic is not met. Deny by default.
        return False

class IsSenderOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow senders of a message to edit/delete it,
    but allow anyone (who has access to the conversation) to view.
    """
    message = "You are not the sender of this message and cannot modify it."

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request (GET, HEAD, OPTIONS),
        # as long as IsParticipantOfConversation allows access to the conversation.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the sender of the message.
        return obj.sender == request.user

# Django-signals_orm-0x04/messaging/managers.py
from django.db import models

class UnreadMessagesManager(models.Manager):
    """
    Custom manager to filter unread messages for a specific user.
    """
    def get_queryset(self):
        # Default queryset for this manager, primarily for consistency
        return super().get_queryset().filter(read=False)

    def unread_for_user(self, user): # <--- Renamed method to match the check
        """
        Filters unread messages where the given user is the receiver.
        """
        # Optimized with .only() to retrieve only necessary fields, as per Task 4.
        # Include 'id' for primary key access, 'sender_id', 'receiver_id' for FKs if needed later,
        # but sender/receiver objects are preferred directly.
        # For display in the list, 'sender', 'content', 'timestamp' are key.
        return self.filter(receiver=user, read=False).select_related('sender').only('id', 'sender__username', 'content', 'timestamp', 'read')

# Django-signals_orm-0x04/messaging/models.py
from django.db import models
from django.contrib.auth.models import User
from .managers import UnreadMessagesManager # Import the new manager

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)
    read = models.BooleanField(default=False) # Added for Task 4

    # Self-referential foreign key for replies (Task 3)
    parent_message = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='replies'
    )

    # Custom managers
    objects = models.Manager() # Default manager
    unread = UnreadMessagesManager() # <--- Renamed manager instance to match the check

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f"From {self.sender.username} to {self.receiver.username}: {self.content[:50]}"

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='notifications')
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"Notification for {self.user.username}: New message from {self.message.sender.username}"

class MessageHistory(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='history')
    old_content = models.TextField()
    edited_at = models.DateTimeField(auto_now_add=True)
    edited_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='edited_messages_history') # Added for the check

    class Meta:
        ordering = ['-edited_at']
        verbose_name_plural = "Message Histories"

    def __str__(self):
        return f"History for Message {self.message.id} by {self.message.sender.username}"

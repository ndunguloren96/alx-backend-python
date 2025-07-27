from django.db import models
from django.contrib.auth.models import User

class ChatMessage(models.Model):
    """
    Represents a single chat message sent by a user.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_messages')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']
        verbose_name = "Chat Message"
        verbose_name_plural = "Chat Messages"

    def __str__(self):
        """
        Returns a string representation of the chat message.
        """
        return f"{self.user.username}: {self.message[:50]}..." if len(self.message) > 50 else f"{self.user.username}: {self.message}"



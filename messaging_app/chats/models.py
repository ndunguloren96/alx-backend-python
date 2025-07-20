import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    """
    Custom User model extending Django's AbstractUser.
    Uses email as the unique identifier instead of username.
    """
    USER_ROLES = (
        ('guest', 'Guest'),
        ('host', 'Host'),
        ('admin', 'Admin'),
    )

    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    # password_hash is handled by Django's AbstractUser set_password method,
    # so we don't define it explicitly here.
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    role = models.CharField(max_length=10, choices=USER_ROLES, default='guest', null=False, blank=False)
    created_at = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number', 'role'] # 'username' is removed

    # Remove the username field if you don't want it at all
    username = None

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        indexes = [
            models.Index(fields=['email']),
        ]


class Conversation(models.Model):
    """
    Model representing a conversation between multiple users.
    """
    conversation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    # Using ManyToManyField with a through model to track participants explicitly.
    # While not strictly required by the current schema for `participants_id`
    # (which implies a single FK), a conversation inherently has multiple participants.
    # A ManyToManyField is the correct way to model this.
    # For simplicity without a dedicated through table model for Participant details,
    # we can define a simple ManyToManyField.
    # If `participants_id` meant a single participant, it would be a ForeignKey.
    # Based on "tracks which users are involved in a conversation", ManyToMany is appropriate.
    participants = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        # Displaying participants for better clarity in admin/debug
        participant_emails = ", ".join([user.email for user in self.participants.all()])
        return f"Conversation {self.conversation_id} with: {participant_emails}"

    class Meta:
        verbose_name = 'Conversation'
        verbose_name_plural = 'Conversations'
        indexes = [
            models.Index(fields=['created_at']),
        ]


class Message(models.Model):
    """
    Model representing a single message within a conversation.
    """
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    message_body = models.TextField(null=False, blank=False)
    sent_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Message from {self.sender.email} in {self.conversation.conversation_id} at {self.sent_at.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
        ordering = ['sent_at'] # Order messages chronologically
        indexes = [
            models.Index(fields=['sender']),
            models.Index(fields=['conversation']),
            models.Index(fields=['sent_at']),
        ]

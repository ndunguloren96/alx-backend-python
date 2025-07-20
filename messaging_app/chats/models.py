import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifier
    for authentication instead of usernames.
    """
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        
        # Extract is_staff and is_active from extra_fields if they exist,
        # otherwise, let them default to False (from AbstractBaseUser) or handle as needed.
        # We need to remove them from extra_fields so they are not passed to user = self.model()
        is_staff = extra_fields.pop('is_staff', False) # Default to False if not provided
        is_active = extra_fields.pop('is_active', True) # Default to True for normal users, common practice

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_staff = is_staff # Set the inherited attribute
        user.is_active = is_active # Set the inherited attribute
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True) # Superusers are usually active by default

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        # Call create_user, which will handle setting is_staff and is_active
        # (after popping them from extra_fields)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User model extending Django's AbstractBaseUser and PermissionsMixin.
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
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    role = models.CharField(max_length=10, choices=USER_ROLES, default='guest', null=False, blank=False)
    created_at = models.DateTimeField(default=timezone.now)

    # Django's AbstractBaseUser already provides 'is_active', 'is_staff', 'is_superuser', 'last_login', 'date_joined' (though 'date_joined' is from AbstractUser, which is why we switched to created_at)
    # So, you do NOT need to define these fields explicitly here, and you should not pass them as custom fields to self.model()
    # is_active = models.BooleanField(default=True) # REMOVE - inherited from AbstractBaseUser
    # is_staff = models.BooleanField(default=False) # REMOVE - inherited from AbstractBaseUser


    # Use the custom manager
    objects = CustomUserManager()

    # Specify email as the unique identifier for authentication
    USERNAME_FIELD = 'email'
    # List of field names that will be prompted for when creating a user via createsuperuser
    # 'email' and 'password' are handled automatically by USERNAME_FIELD and password handling
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number', 'role'] 

    # Correctly remove the username field if you don't want it from AbstractUser
    # You're inheriting from AbstractBaseUser now, so username is not a concern,
    # but explicitly setting it to None if you were using AbstractUser would be correct.
    # Since you changed to AbstractBaseUser, this specific line (username = None)
    # is not strictly necessary but harmless.
    # username = None 

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
    participants = models.ManyToManyField('User', related_name='conversations') # Use string reference for User
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        if self.pk:
            participant_emails = ", ".join([user.email for user in self.participants.all()])
        else:
            participant_emails = "New Conversation"
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
    sender = models.ForeignKey('User', on_delete=models.CASCADE, related_name='sent_messages') # Use string reference for User
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    message_body = models.TextField(null=False, blank=False)
    sent_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Message from {self.sender.email} in {self.conversation.conversation_id} at {self.sent_at.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
        ordering = ['sent_at']
        indexes = [
            models.Index(fields=['sender']),
            models.Index(fields=['conversation']),
            models.Index(fields=['sent_at']),
        ]

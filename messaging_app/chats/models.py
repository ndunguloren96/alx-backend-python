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
        
        # is_staff and is_active are now explicitly defined as models.BooleanField fields
        # in the User model below. When extra_fields is passed to self.model(),
        # these values will correctly set the corresponding model fields.
        # Therefore, we no longer need to pop them or set them manually here.

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True) 

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
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

    # Re-add these fields explicitly. 
    # While PermissionsMixin provides them as attributes,
    # Django's Admin often requires them as explicit model fields 
    # for list_display and list_filter to work seamlessly.
    # Also, having them as explicit fields ensures they are properly
    # created in the database schema.
    is_active = models.BooleanField(default=True) 
    is_staff = models.BooleanField(default=False)
    # is_superuser is provided by PermissionsMixin and typically doesn't need
    # to be explicitly redefined as a models.BooleanField.


    # Use the custom manager
    objects = CustomUserManager()

    # Specify email as the unique identifier for authentication
    USERNAME_FIELD = 'email'
    # List of field names that will be prompted for when creating a user via createsuperuser
    # 'email' and 'password' are handled automatically by USERNAME_FIELD and password handling
    # 'is_active', 'is_staff', 'is_superuser' are typically handled by create_superuser's defaults
    # but since we explicitly defined is_active and is_staff, they will be handled by the manager
    # when passed through extra_fields.
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number', 'role'] 

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

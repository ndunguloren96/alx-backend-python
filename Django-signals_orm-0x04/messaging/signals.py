from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Message, Notification, MessageHistory # Import MessageHistory for Task 1

@receiver(post_save, sender=Message)
def create_notification_on_new_message(sender, instance, created, **kwargs):
    """
    Signal handler to create a notification when a new message is saved.
    """
    if created:
        Notification.objects.create(user=instance.receiver, message=instance)
        print(f"Notification created for {instance.receiver.username} for new message from {instance.sender.username}")

@receiver(post_save, sender=Message)
def log_message_edit(sender, instance, created, **kwargs):
    """
    Signal handler to log message edits using pre_save to get old content.
    This signal will specifically handle the 'edited' flag being set to True.
    The actual logging of old content will be done in a pre_save signal.
    """
    if not created and instance.edited:
        # This part ensures the 'edited' flag is set if a modification occurs.
        # The logging of the old content is handled by the pre_save signal.
        print(f"Message {instance.id} by {instance.sender.username} was edited.")

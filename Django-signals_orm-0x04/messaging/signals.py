from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User # Import User model
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

@receiver(pre_save, sender=Message)
def log_message_old_content(sender, instance, **kwargs):
    """
    Signal handler to save the old content of a message before it's updated.
    """
    if instance.pk: # Check if the instance already exists (i.e., it's an update, not a creation)
        try:
            old_instance = sender.objects.get(pk=instance.pk)
            if old_instance.content != instance.content:
                MessageHistory.objects.create(message=instance, old_content=old_instance.content)
                instance.edited = True # Set edited flag when content changes
                print(f"Message {instance.id} old content saved to history.")
        except sender.DoesNotExist:
            pass # Object is new, or not found (shouldn't happen for updates)



@receiver(post_delete, sender=User)
def cleanup_user_data(sender, instance, **kwargs):
    """
    Signal handler to clean up all associated data when a User is deleted.
    Note: With CASCADE delete on ForeignKeys, much of this is handled automatically.
    This signal serves to confirm or perform additional non-cascading cleanup.
    """
    # Messages sent by the user will be deleted by CASCADE on Message.sender
    # Messages received by the user will be deleted by CASCADE on Message.receiver
    # Notifications for the user will be deleted by CASCADE on Notification.user
    # MessageHistory entries will be deleted by CASCADE if their associated Message is deleted.

    # Example of what you *could* do if CASCADE wasn't used or for other actions:
    # Message.objects.filter(Q(sender=instance) | Q(receiver=instance)).delete()
    # Notification.objects.filter(user=instance).delete()
    # No need to explicitly delete MessageHistory here if Message has CASCADE

    print(f"User {instance.username} (ID: {instance.id}) deleted. Associated data (messages, notifications) are handled by CASCADE or custom logic.")

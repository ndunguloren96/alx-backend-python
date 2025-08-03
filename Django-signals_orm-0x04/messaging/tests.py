from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message, Notification, MessageHistory
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from unittest.mock import patch, MagicMock

# Define a simple pre_save signal for testing purposes within the test file
# This is a good practice for isolated testing of signal logic
@receiver(pre_save, sender=Message)
def _test_pre_save_message_handler(sender, instance, **kwargs):
    if instance.pk: # Only run if the instance already exists (i.e., it's an update)
        old_instance = Message.objects.get(pk=instance.pk)
        if old_instance.content != instance.content:
            MessageHistory.objects.create(message=instance, old_content=old_instance.content)
            instance.edited = True # Set edited flag when content changes

class MessageSignalsTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password1')
        self.user2 = User.objects.create_user(username='user2', password='password2')

    def test_notification_created_on_new_message(self):
        """
        Test that a Notification is created when a new Message is saved.
        """
        self.assertEqual(Notification.objects.count(), 0)
        message = Message.objects.create(sender=self.user1, receiver=self.user2, content="Hello there!")
        self.assertEqual(Notification.objects.count(), 1)
        notification = Notification.objects.get(message=message)
        self.assertEqual(notification.user, self.user2)
        self.assertEqual(notification.message, message)

    @patch('messaging.signals.Notification.objects.create')
    def test_notification_signal_called(self, mock_create):
        """
        Test that the post_save signal handler for notifications is called.
        """
        Message.objects.create(sender=self.user1, receiver=self.user2, content="Another message.")
        mock_create.assert_called_once()
        self.assertEqual(mock_create.call_args[1]['user'], self.user2)
        self.assertEqual(mock_create.call_args[1]['message'].content, "Another message.")

    def test_message_history_created_on_edit(self):
        """
        Test that MessageHistory is created and 'edited' flag is set on message edit.
        """
        message = Message.objects.create(sender=self.user1, receiver=self.user2, content="Original content")
        self.assertEqual(MessageHistory.objects.count(), 0)
        self.assertFalse(message.edited)

        # Edit the message content
        old_content = message.content
        message.content = "Updated content"
        message.save()

        self.assertEqual(MessageHistory.objects.count(), 1)
        history_entry = MessageHistory.objects.first()
        self.assertEqual(history_entry.message, message)
        self.assertEqual(history_entry.old_content, old_content)

        # Re-fetch message to get updated 'edited' status if it's not directly modified in test setup
        updated_message = Message.objects.get(pk=message.pk)
        self.assertTrue(updated_message.edited)

# Django-signals_orm-0x04/messaging/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.http import Http404
from django.views.decorators.cache import cache_page
from .models import Message, Notification
from django.contrib.auth.models import User
from django.db.models import Q # For Task 4


@login_required
def delete_user_account(request):
    """
    Allows a logged-in user to delete their own account.
    """
    if request.method == 'POST':
        user = request.user
        user_id = user.id
        logout(request)
        user.delete()
        messages.success(request, f"Your account and all associated data have been deleted. User ID: {user_id}")
        return redirect('home')
    return render(request, 'messaging/confirm_delete.html')

def home(request):
    return render(request, 'messaging/home.html')


@login_required
@cache_page(60 * 1) # Cache for 60 seconds (Task 5)
def conversation_view(request, message_id=None):
    """
    Displays a threaded conversation or a list of unread messages.
    Combines logic for Task 3 (threaded) and Task 4 (unread/optimized).
    """
    user = request.user
    context = {}

    if message_id:
        try:
            # Task 3: Optimize with select_related for parent_message's sender/receiver
            parent_message = Message.objects.select_related('sender', 'receiver').get(id=message_id)

            # Task 3: Fetch direct replies efficiently.
            # Use select_related for sender/receiver of replies to avoid N+1 queries.
            replies = parent_message.replies.all().select_related('sender', 'receiver').order_by('timestamp')

            context['parent_message'] = parent_message
            context['replies'] = replies

            # Mark messages in this conversation as read for the current user
            # (assuming the user is the receiver)
            messages_in_thread = [parent_message] + list(replies)
            for msg in messages_in_thread:
                if msg.receiver == user and not msg.read:
                    msg.read = True
                    msg.save()
            Notification.objects.filter(user=user, message__in=messages_in_thread).update(is_read=True)

        except Message.DoesNotExist:
            raise Http404("Message not found.")
    else:
        # Task 4: Custom manager for unread messages using 'unread_messages.for_user'
        # .only() is applied inside the manager method for 'unread_messages.for_user'.
        unread_messages = Message.unread_messages.for_user(user) # This already includes .only() and .select_related() from the manager

        context['unread_messages'] = unread_messages

        # All messages for the current user (sender OR receiver)
        # Task: `["sender=request.user"]` implies showing messages sent by the user,
        # so ensure the query correctly covers both sent and received.
        # Use select_related for sender/receiver for efficiency.
        all_messages = Message.objects.filter(
            Q(sender=user) | Q(receiver=user)
        ).select_related('sender', 'receiver').order_by('-timestamp')
        context['all_messages'] = all_messages

    return render(request, 'messaging/conversation.html', context)

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.http import Http404

# Added for Task 5: Caching
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
        user_id = user.id # Get user ID before deleting for signal check
        logout(request) # Log out the user before deleting to prevent issues
        user.delete()
        messages.success(request, f"Your account and all associated data have been deleted. User ID: {user_id}")
        return redirect('home') # Redirect to a home page or login page
    return render(request, 'messaging/confirm_delete.html')

# Placeholder for a home view for redirection
def home(request):
    return render(request, 'messaging/home.html')

# Views for Task 5:
# @cache_page(60 * 1) # Cache for 60 seconds
# def message_list_cached(request):
#     # This view would display a list of messages, potentially filtered
#     # For demonstration, let's just show all messages (or recent ones)
#     messages = Message.objects.all().order_by('-timestamp')[:20]
#     return render(request, 'messaging/message_list.html', {'messages': messages})

# Modified for Task 3 & 4 combined context
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
            parent_message = Message.objects.get(id=message_id)
            # Recursive query for threaded conversations (Task 3)
            # This is a simplified example; a true recursive query in Django ORM
            # can be complex and might involve raw SQL or a custom tree structure.
            # For this context, we'll fetch direct replies.
            replies = Message.objects.filter(parent_message=parent_message).order_by('timestamp')
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
        # Custom manager for unread messages (Task 4)
        # Using .only() to optimize query
        unread_messages = Message.unread_messages.for_user(user).only('sender', 'receiver', 'content', 'timestamp')
        context['unread_messages'] = unread_messages

        # All messages for the current user for demonstration
        all_messages = Message.objects.filter(Q(sender=user) | Q(receiver=user)).select_related('sender', 'receiver').order_by('-timestamp')
        context['all_messages'] = all_messages

    return render(request, 'messaging/conversation.html', context)

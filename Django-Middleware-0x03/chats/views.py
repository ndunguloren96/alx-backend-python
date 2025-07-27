from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import ChatMessage
from django.contrib.auth.models import User # Import User model for dummy roles

# This is a simple message box function to replace alert()
# In a real application, you would render a template with the message.
def message_box(request, message, status_code=200):
    """
    Renders a simple HTML page with a message.
    Used to replace alert() for displaying errors or confirmations.
    """
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Message</title>
        <style>
            body {{ font-family: sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; background-color: #f0f0f0; margin: 0; }}
            .message-container {{ background-color: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); text-align: center; max-width: 400px; }}
            h1 {{ color: #333; }}
            p {{ color: #666; }}
            a {{ display: inline-block; margin-top: 20px; padding: 10px 20px; background-color: #007bff; color: white; text-decoration: none; border-radius: 5px; }}
            a:hover {{ background-color: #0056b3; }}
        </style>
    </head>
    <body>
        <div class="message-container">
            <h1>Notification</h1>
            <p>{message}</p>
            <a href="/chats/">Go Back to Chat</a>
        </div>
    </body>
    </html>
    """
    return HttpResponseForbidden(html_content, status=status_code)


@login_required # Ensure user is logged in to access chat
def chat_view(request):
    """
    Handles displaying chat messages and submitting new ones.
    """
    # For demonstration of RolePermissionMiddleware:
    # You can set a dummy role for the current user for testing.
    # In a real app, roles would come from a user profile or permissions system.
    if not hasattr(request.user, 'role'):
        # Assign a default 'user' role if not set.
        # For testing, you can modify this to 'admin' or 'moderator'
        # e.g., if request.user.username == 'adminuser': request.user.role = 'admin'
        request.user.role = 'user' # Default role for demonstration

    if request.method == 'POST':
        message_content = request.POST.get('message')
        if message_content:
            ChatMessage.objects.create(user=request.user, message=message_content)
            return redirect('chat_view') # Redirect to prevent resubmission on refresh
        else:
            return message_box(request, "Message cannot be empty.", 400)

    messages = ChatMessage.objects.all()
    return render(request, 'chats/chat.html', {'messages': messages})



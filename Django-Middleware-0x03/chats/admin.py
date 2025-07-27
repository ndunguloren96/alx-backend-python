from django.contrib import admin
from .models import ChatMessage

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    """
    Admin configuration for the ChatMessage model.
    Displays user, message, and timestamp in the list view.
    Allows searching by user and message.
    """
    list_display = ('user', 'message', 'timestamp')
    search_fields = ('user__username', 'message')
    list_filter = ('timestamp',)



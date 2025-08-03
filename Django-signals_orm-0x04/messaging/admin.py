from django.contrib import admin
from .models import Message, Notification, MessageHistory # Import MessageHistory for Task 1

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'content', 'timestamp', 'edited')
    list_filter = ('sender', 'receiver', 'timestamp', 'edited')
    search_fields = ('content',)

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'is_read', 'timestamp')
    list_filter = ('user', 'is_read', 'timestamp')
    search_fields = ('message__content',)

@admin.register(MessageHistory) # Register MessageHistory for Task 1
class MessageHistoryAdmin(admin.ModelAdmin):
    list_display = ('message', 'old_content', 'edited_at')
    list_filter = ('message__sender', 'message__receiver', 'edited_at')
    search_fields = ('old_content',)

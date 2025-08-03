# Django-signals_orm-0x04/messaging/admin.py
from django.contrib import admin
from .models import Message, Notification, MessageHistory

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'content', 'timestamp', 'edited', 'read', 'parent_message')
    list_filter = ('sender', 'receiver', 'timestamp', 'edited', 'read')
    search_fields = ('content',)
    raw_id_fields = ('parent_message',) # Useful for self-referential FK

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'is_read', 'timestamp')
    list_filter = ('user', 'is_read', 'timestamp')
    search_fields = ('message__content',)

@admin.register(MessageHistory)
class MessageHistoryAdmin(admin.ModelAdmin):
    list_display = ('message', 'old_content', 'edited_by', 'edited_at') # Added edited_by
    list_filter = ('message__sender', 'message__receiver', 'edited_by', 'edited_at') # Added edited_by
    search_fields = ('old_content',)

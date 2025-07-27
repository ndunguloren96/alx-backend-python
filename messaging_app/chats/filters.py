# messaging_app/chats/filters.py

import django_filters
from .models import Message, Conversation
from django.db.models import Q # Import Q object for complex lookups

class MessageFilter(django_filters.FilterSet):
    """
    Filter for messages, allowing filtering by sent_at date range.
    """
    sent_at_before = django_filters.DateTimeFilter(field_name="sent_at", lookup_expr='lte')
    sent_at_after = django_filters.DateTimeFilter(field_name="sent_at", lookup_expr='gte')

    # Add optional filtering by sender email if needed, though 'sender' is already in filterset_fields
    # For filtering conversations by specific users, that's better handled in ConversationFilter
    # if you were to create one, or directly via 'participants' field on ConversationViewSet.

    class Meta:
        model = Message
        fields = ['sender', 'conversation', 'sent_at'] # Keep existing fields for basic filtering

class ConversationFilter(django_filters.FilterSet):
    """
    Filter for conversations, allowing filtering by participants.
    """
    # Allows filtering by multiple participant IDs, e.g., ?participants=uuid1&participants=uuid2
    participants = django_filters.ModelMultipleChoiceFilter(
        field_name='participants',
        queryset=Conversation.objects.none(), # This queryset will be overridden in the view
        conjoined=True # Requires all specified participants to be in the conversation
    )
    # Filter by created_at range
    created_before = django_filters.DateTimeFilter(field_name="created_at", lookup_expr='lte')
    created_after = django_filters.DateTimeFilter(field_name="created_at", lookup_expr='gte')

    class Meta:
        model = Conversation
        fields = ['participants', 'created_at']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Dynamically set the queryset for participants filter to include all users
        # This prevents issues if the initial queryset is empty and no choices are displayed
        from .models import User
        self.filters['participants'].queryset = User.objects.all()

from rest_framework import serializers
from .models import User, Conversation, Message
from django.db import models # Import models module for specific field types

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the Custom User model.
    Omits sensitive fields like password.
    """
    class Meta:
        model = User
        fields = ('user_id', 'email', 'first_name', 'last_name', 'phone_number', 'role', 'created_at')
        read_only_fields = ('user_id', 'email', 'created_at') # Email should not be changed after creation via API

# Nested serializer for messages within a conversation
class MessageSerializer(serializers.ModelSerializer):
    # Use CharField for sender's email for readability in the nested output
    sender_email = serializers.ReadOnlyField(source='sender.email')

    class Meta:
        model = Message
        fields = ('message_id', 'sender', 'sender_email', 'conversation', 'message_body', 'sent_at')
        read_only_fields = ('message_id', 'conversation', 'sent_at') # conversation is set by the parent view
        extra_kwargs = {'sender': {'write_only': True}} # sender is provided during creation, but not read back as ID

# Main serializer for Conversation
class ConversationSerializer(serializers.ModelSerializer):
    # messages is a Reverse relationship, so we need to define it explicitly
    # Read_only because messages are created via a nested endpoint, not directly here
    messages = MessageSerializer(many=True, read_only=True)
    
    # You can also add a field to display participant emails for readability
    participant_emails = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ('conversation_id', 'participants', 'participant_emails', 'created_at', 'messages')
        read_only_fields = ('conversation_id', 'created_at')

    # Method to get participant emails for the participant_emails field
    def get_participant_emails(self, obj):
        return [user.email for user in obj.participants.all()]

    def validate_participants(self, value):
        # Ensure there are at least two participants for a conversation
        if not value or len(value) < 2:
            raise serializers.ValidationError("A conversation must have at least two participants.")
        return value

    def create(self, validated_data):
        participants_data = validated_data.pop('participants')
        conversation = Conversation.objects.create(**validated_data)
        conversation.participants.set(participants_data) # Use set() for ManyToMany
        return conversation

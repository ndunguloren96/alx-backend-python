from rest_framework import serializers
from .models import User, Conversation, Message

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the Custom User model.
    Excludes sensitive fields like password_hash.
    """
    class Meta:
        model = User
        fields = ['user_id', 'first_name', 'last_name', 'email', 'phone_number', 'role', 'created_at']
        read_only_fields = ['user_id', 'created_at']

class MessageSerializer(serializers.ModelSerializer):
    """
    Serializer for the Message model.
    Nests the UserSerializer for the sender to show sender details.
    """
    sender = UserSerializer(read_only=True) # Nested serializer for sender

    class Meta:
        model = Message
        fields = ['message_id', 'sender', 'conversation', 'message_body', 'sent_at']
        read_only_fields = ['message_id', 'sent_at']
        extra_kwargs = {
            'conversation': {'write_only': True} # conversation field is typically set internally when creating messages for a specific conversation
        }


class ConversationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Conversation model.
    Nests UserSerializer for participants and MessageSerializer for messages.
    """
    # Nested serializer for participants, allows writing only user_id for creation
    participants = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), many=True
    )
    messages = MessageSerializer(many=True, read_only=True) # Nested serializer for messages, read-only as messages are created separately

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'messages', 'created_at']
        read_only_fields = ['conversation_id', 'created_at']

    def create(self, validated_data):
        participants_data = validated_data.pop('participants')
        conversation = Conversation.objects.create(**validated_data)
        conversation.participants.set(participants_data) # Use set for ManyToMany
        return conversation

    def update(self, instance, validated_data):
        # Handle participants update if needed
        participants_data = validated_data.pop('participants', None)
        if participants_data is not None:
            instance.participants.set(participants_data)

        # Update other fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

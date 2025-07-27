# messaging_app/chats/auth.py

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Customizes the JWT Token response to include user details in the token payload
    and directly in the response body.
    """
    @classmethod
    def get_token(cls, user):
        """
        Overrides the default get_token to add custom claims to the JWT payload.
        These claims can be decoded from the JWT token itself on the client side.
        """
        token = super().get_token(user)

        # Add custom claims to the token payload
        token['user_id'] = str(user.user_id) # Ensure UUID is stringified
        token['email'] = user.email
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['role'] = user.role
        # Add any other user fields you want directly accessible in the token payload
        # For security, avoid putting sensitive information directly in the token payload.

        return token

    def validate(self, attrs):
        """
        Overrides the default validate method to add extra user details
        to the login response body.
        """
        # Call the default validate method to perform authentication and get tokens
        data = super().validate(attrs)

        # Add extra user details to the response data
        data['user'] = {
            'user_id': str(self.user.user_id),
            'email': self.user.email,
            'first_name': self.user.first_name,
            'last_name': self.user.last_name,
            'phone_number': self.user.phone_number, # Include phone number from your model
            'role': self.user.role,
            'created_at': self.user.created_at.isoformat(), # Use ISO 8601 format for datetime
            'is_staff': self.user.is_staff,
            'is_superuser': self.user.is_superuser,
        }
        return data

# serializers.py
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        # Get the original token
        token = super().get_token(user)

        # Add custom claims
        token['user_id'] = user.id
        token['is_superuser'] = user.is_superuser  # Adds is_superuser to the token payload
        token['is_staff'] = user.is_staff          # Adds is_staff to the token payload

        return token

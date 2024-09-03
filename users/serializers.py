from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username','first_name','last_name','email','password','phone_number','address','date_of_birth','emergency_contact_name','emergency_contact_phone','profile_picture'] # Serialize all fields of the Product model
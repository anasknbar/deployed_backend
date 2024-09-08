from rest_framework import serializers, viewsets
from .models import ComplaintRequest

class ComplaintRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplaintRequest
        fields = ['id','user_name','phone_number','address','subject', 'message', 'category', 'priority','created_at','response']



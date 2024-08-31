from rest_framework import serializers
from .models import LeaseAgreement

class LeaseAgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaseAgreement
        fields = '__all__'  # Serialize all fields of the Product model
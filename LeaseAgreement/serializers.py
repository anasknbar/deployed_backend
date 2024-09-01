from rest_framework import serializers
from .models import LeaseAgreement

class LeaseAgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaseAgreement
        fields = ['tenant','property','rent_amount','security_deposit','payment_frequency','lease_terms','is_active','created_at','created_at','lease_start_date','lease_end_date'] # Serialize all fields of the Product model
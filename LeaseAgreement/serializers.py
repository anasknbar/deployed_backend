from rest_framework import serializers
from .models import LeaseAgreement

class LeaseAgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaseAgreement
        fields = ['id','tenant','property','rent_amount','security_deposit','payment_frequency','lease_terms','is_active','created_at','created_at','lease_start_date','lease_end_date'] # Serialize all fields of the Product model
        
class LeaseAgreementSerializerWithNames(serializers.ModelSerializer):
    tenant_name = serializers.CharField(source='tenant.username', read_only=True)
    property_name = serializers.CharField(source='property.name', read_only=True)
    class Meta:
        model = LeaseAgreement
        fields = ['id','tenant_name','property_name','rent_amount','security_deposit','payment_frequency','lease_terms','is_active','created_at','created_at','lease_start_date','lease_end_date'] # Serialize all fields of the Product model
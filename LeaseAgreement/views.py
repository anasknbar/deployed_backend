from django.shortcuts import render
from .models import LeaseAgreement
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import LeaseAgreementSerializer,LeaseAgreementSerializerWithNames
# Create your views here.

class LeaseAgreementListView(ListAPIView):

  queryset = LeaseAgreement.objects.all()
  serializer_class = LeaseAgreementSerializer

class LeaseAgreementListViewWithNames(ListAPIView):

  queryset = LeaseAgreement.objects.all()
  serializer_class = LeaseAgreementSerializerWithNames
  
class LeaseAgreementCreateView(CreateAPIView):
  queryset = LeaseAgreement.objects.all()
  serializer_class = LeaseAgreementSerializer
  
class LeaseAgreementDetailView(RetrieveUpdateDestroyAPIView):
  queryset = LeaseAgreement.objects.all()
  serializer_class = LeaseAgreementSerializer


# ------------------------
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import LeaseAgreement
from .serializers import LeaseAgreementSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
 
# API views for LeaseAgreement
 # View for checking expiring leases
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check_expiring_leases(request):
    today = timezone.now().date()
    user = request.user  # Get the currently logged-in user
 
    # Filter leases for the current user
    leases = LeaseAgreement.objects.filter(tenant=user)
    lease_data = []
 
    for lease in leases:
        end_date = lease.lease_end_date
        if end_date:
            if end_date == today:
                lease_data.append({
                    'property': lease.property.name,
                    'lease_end_date': end_date,
                    'status': 'expired'
                })
            elif end_date > today:
                days_remaining = (end_date - today).days
                lease_data.append({
                    'property': lease.property.name,
                    'lease_end_date': end_date,
                    'days_remaining': days_remaining,
                    'status': 'active'
                })
 
    return Response({'leases': lease_data})
 
# View for checking overdue payments
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def overdue_payments(request):
    today = timezone.now().date()
    user = request.user  # Get the currently logged-in user
 
    # Filter overdue leases for the current user
    overdue_leases = LeaseAgreement.objects.filter(
        tenant=user,
        lease_end_date__gt=today,
        last_paid_date__isnull=False
    )
   
    lease_data = []
 
    for lease in overdue_leases:
        if lease.payment_frequency == 'MONTHLY' and lease.last_paid_date <= today - timedelta(days=30):
            lease_data.append({
                'property': lease.property.name,
                'tenant': lease.tenant.username,
                'amount_due': lease.rent_amount,
                'last_paid_date': lease.last_paid_date,
                'status': 'overdue'
            })
        elif lease.payment_frequency == 'YEARLY' and lease.last_paid_date <= today - timedelta(days=365):
            lease_data.append({
                'property': lease.property.name,
                'tenant': lease.tenant.username,
                'amount_due': lease.rent_amount,
                'last_paid_date': lease.last_paid_date,
                'status': 'overdue'
            })
 
    return Response({'overdue_payments': lease_data})
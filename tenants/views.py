from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView,ListCreateAPIView
from .models import Tenant
from .serializers import TenantSerializer
# Create your views here.

class TenantListView(ListAPIView):

  queryset = Tenant.objects.all()
  serializer_class = TenantSerializer
  
class TenantCreateView(CreateAPIView):
  queryset = Tenant.objects.all()
  serializer_class = TenantSerializer
  
class TenantDetailView(RetrieveUpdateDestroyAPIView):
  queryset = Tenant.objects.all()
  serializer_class = TenantSerializer
  

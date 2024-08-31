from django.shortcuts import render
from .models import LeaseAgreement
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import LeaseAgreementSerializer
# Create your views here.

class LeaseAgreementListView(ListAPIView):

  queryset = LeaseAgreement.objects.all()
  serializer_class = LeaseAgreementSerializer
  
class LeaseAgreementCreateView(CreateAPIView):
  queryset = LeaseAgreement.objects.all()
  serializer_class = LeaseAgreementSerializer
  
class LeaseAgreementDetailView(RetrieveUpdateDestroyAPIView):
  queryset = LeaseAgreement.objects.all()
  serializer_class = LeaseAgreementSerializer

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

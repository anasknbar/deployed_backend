from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from .models import ComplaintRequest
from .serializers import ComplaintRequestSerializer
# Create your views here.

class ComplaintsListView(ListAPIView):

  queryset = ComplaintRequest.objects.all()
  serializer_class = ComplaintRequestSerializer
  
class ComplaintsCreateView(CreateAPIView):
  queryset = ComplaintRequest.objects.all()
  serializer_class = ComplaintRequestSerializer
  
class ComplaintsDetailView(RetrieveUpdateDestroyAPIView):
  queryset = ComplaintRequest.objects.all()
  serializer_class = ComplaintRequestSerializer



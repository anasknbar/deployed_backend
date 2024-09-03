from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Property
from .serializers import PropertySerializer
# Create your views here.

class PropertyListView(ListAPIView):

  queryset = Property.objects.all()
  serializer_class = PropertySerializer
  
class PropertyCreateView(CreateAPIView):
  queryset = Property.objects.all()
  serializer_class = PropertySerializer
  
class PropertyDetailView(RetrieveUpdateDestroyAPIView):
  queryset = Property.objects.all()
  serializer_class = PropertySerializer
from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.

class UserListView(ListAPIView):
  pass

class UserDetailView(CreateAPIView):
  pass

class UserCreateView(RetrieveUpdateDestroyAPIView):
  pass

from rest_framework import viewsets
from django.contrib.auth.models import User  # Or import CustomUser if you have a custom model
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import permission_classes
from .serializers import UserSerializer

@permission_classes([IsAdminUser])
class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()


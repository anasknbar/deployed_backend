from django.shortcuts import render
from .models import CustomUser
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import UserSerializer
# Create your views here.

class UsersListView(ListAPIView):

  queryset = CustomUser.objects.all()
  serializer_class = UserSerializer
  
class UserCreateView(CreateAPIView):
  queryset = CustomUser.objects.all()
  serializer_class = UserSerializer
  
class UserDetailView(RetrieveUpdateDestroyAPIView):
  queryset = CustomUser.objects.all()
  serializer_class = UserSerializer

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
#--------------------------------------------------
from rest_framework.response import Response
from rest_framework import status
from tenants.models import Tenant
from tenants.serializers import TenantSerializer
from users.serializers import UserSerializer

@permission_classes([IsAdminUser])
class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
    def create(self, request, *args, **kwargs):
        user_serializer = self.get_serializer(data=request.data)
        
        if user_serializer.is_valid():
            # Save user instance
            user = user_serializer.save()
            
            # Prepare tenant data
            tenant_data = {
                "user": user.id,
                "phone_number": request.data.get("phone_number"),
                "date_of_birth": request.data.get("date_of_birth"),
                "emergency_contact_name": request.data.get("emergency_contact_name"),
                "emergency_contact_phone": request.data.get("emergency_contact_phone"),
            }
            
            # Validate and save tenant data
            tenant_serializer = TenantSerializer(data=tenant_data)
            if tenant_serializer.is_valid():
                tenant_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_201_CREATED)
            
            # If tenant data is invalid, delete the created user to prevent orphaned records
            user.delete()
            return Response(tenant_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


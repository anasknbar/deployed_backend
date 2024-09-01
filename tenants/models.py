from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tenant(models.Model):
  
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='tenant_profile')

    phone_number = models.CharField(max_length=15,blank=True,null=True)
    date_of_birth = models.DateField(blank=True,null=True)
    emergency_contact_name = models.CharField(max_length=100, null=True, blank=True)
    emergency_contact_phone = models.CharField(max_length=15, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f"{self.user}"


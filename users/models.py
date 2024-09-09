from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15,blank=True,null=True)
    address = models.CharField(max_length=15,blank=True,null=True)
    date_of_birth = models.DateField(blank=True,null=True)
    emergency_contact_name = models.CharField(max_length=100, null=True, blank=True)
    emergency_contact_phone = models.CharField(max_length=15, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    pass
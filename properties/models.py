from django.db import models
from django.contrib.auth.models import User  # Assuming you're using the default User model for property owners
from tenants.models import Tenant  # Import Tenant model if defined in another app
from LeaseAgreement.models import LeaseAgreement
# Create your models here.


from django.conf import settings
# Define choices for property types
PROPERTY_TYPE_CHOICES = [
    ('APARTMENT', 'Apartment'),
    ('HOUSE', 'House'),
    ('COMMERCIAL', 'Commercial'),
    ('CONDO', 'Condo'),
    ('TOWNHOUSE', 'Townhouse'),
    ('OTHER', 'Other'),
]

class Property(models.Model):

    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    property_type = models.CharField(max_length=50, choices=PROPERTY_TYPE_CHOICES)
    available_from = models.DateField()
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties') # based on the owner.
    # owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='properties')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tenants = models.ManyToManyField(Tenant, through='LeaseAgreement.LeaseAgreement', related_name='properties_rented') # check it with teams if it's a good idea

    def __str__(self):
        return f"{self.name} ({self.address})"


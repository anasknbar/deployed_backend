from django.db import models

# Create your models here.
from django.conf import settings
class LeaseAgreement(models.Model):
    
    tenant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='lease_agreements')
    property = models.ForeignKey('properties.Property', on_delete=models.CASCADE, related_name='lease_agreements')
    lease_start_date = models.DateField()
    lease_end_date = models.DateField(null=True, blank=True)
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    security_deposit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    payment_frequency = models.CharField(max_length=20, choices=[('MONTHLY', 'Monthly'), ('YEARLY', 'Yearly')])
    lease_terms = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_paid_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Lease Agreement for {self.tenant} at {self.property}"

from django.db import models

# Create your models here.
from django.db import models

class ComplaintRequest(models.Model):
    # No need for a user field in the model
    user_name = models.CharField(max_length=15,blank=True,null=True)
    phone_number = models.CharField(max_length=15,blank=True,null=True)
    address = models.CharField(max_length=15,blank=True,null=True)
    
    subject = models.CharField(max_length=255)
    message = models.TextField()
    category = models.CharField(max_length=100, choices=[
        ('maintenance', 'Maintenance'),
        ('payment', 'Payment'),
        ('noise', 'Noise Complaint'),
        ('other', 'Other')
    ], blank=True, null=True)
    priority = models.CharField(max_length=50, choices=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ], blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    response = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.subject}'

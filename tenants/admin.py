from django.contrib import admin
from .models import Tenant
# Register your models here.
class AdminTenant(admin.ModelAdmin):
  list_display = ['first_name','last_name','email','phone_number','date_of_birth','lease_start_date','lease_end_date','rent_amount','is_active','emergency_contact_name','emergency_contact_phone','created_at','updated_at']
admin.site.register(Tenant)
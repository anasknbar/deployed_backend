from django.contrib import admin
from .models import LeaseAgreement
# Register your models here.

class AdminLeaseAgreement(admin.ModelAdmin):
  list_display = ['tenant','property','lease_start_date','lease_end_date','rent_amount','is_active']
admin.site.register(LeaseAgreement,AdminLeaseAgreement)



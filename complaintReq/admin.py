from django.contrib import admin
from .models import ComplaintRequest
# Register your models here.

class AdminComplaints(admin.ModelAdmin):
  list_display =  ['subject','message','category','priority','created_at','updated_at']
admin.site.register(ComplaintRequest,AdminComplaints)

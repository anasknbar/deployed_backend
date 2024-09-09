from django.contrib import admin
from .models import Property
# from .models import LeaseAgreement
# Register your models here.

class AdminProperty(admin.ModelAdmin):
  list_display = ['name','address','city','state','postal_code','country','property_type','available_from','description','owner','created_at','updated_at'] # ,'number_of_units'

admin.site.register(Property,AdminProperty)
# admin.site.register(LeaseAgreement)

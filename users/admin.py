from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Add the fields you want to display in the admin interface
    list_display = ('username', 'email', 'is_staff', 'is_active','date_joined')
    
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'address', 'date_of_birth','emergency_contact_name','emergency_contact_phone')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number', 'address', 'date_of_birth','emergency_contact_name','emergency_contact_phone')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

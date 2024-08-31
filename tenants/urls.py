from django.urls import path
from .views import TenantListView,TenantDetailView,TenantCreateView
urlpatterns = [
  path('',TenantListView.as_view(),name='tenants'),
  path('create',TenantCreateView.as_view(),name='create_property'),
  path('<int:pk>',TenantDetailView.as_view(),name='property_details' )
]
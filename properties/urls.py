from django.urls import path

from .views import PropertyListView,PropertyCreateView,PropertyDetailView
urlpatterns = [
  path('',PropertyListView.as_view(),name='tenants'),
  path('create/',PropertyCreateView.as_view(),name='create'),
  path('<int:pk>',PropertyDetailView.as_view(),name='details' )
]
from django.urls import path

from .views import PropertyListView,PropertyCreateView,PropertyDetailView
urlpatterns = [
  path('',PropertyListView.as_view(),name='properties'),
  path('create/',PropertyCreateView.as_view(),name='create-property'),
  path('<int:pk>',PropertyDetailView.as_view(),name='property-details' )
]
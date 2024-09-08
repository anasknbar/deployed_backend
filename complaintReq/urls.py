from django.urls import path

from .views import ComplaintsListView,ComplaintsCreateView,ComplaintsDetailView
urlpatterns = [
  path('',ComplaintsListView.as_view(),name='complaints'),
  path('create/',ComplaintsCreateView.as_view(),name='create-complaint'),
  path('<int:pk>',ComplaintsDetailView.as_view(),name='complaint-details' )
]
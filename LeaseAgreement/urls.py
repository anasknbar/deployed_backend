from django.urls import path

from .views import LeaseAgreementListView,LeaseAgreementCreateView,LeaseAgreementDetailView
urlpatterns = [
  path('',LeaseAgreementListView.as_view(),name='tenants'),
  path('create/',LeaseAgreementCreateView.as_view(),name='create_lease_agr'),
  path('<int:pk>',LeaseAgreementDetailView.as_view(),name='lease_agr_details' )
]
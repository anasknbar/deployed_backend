from django.urls import path

from .views import UsersListView,UserCreateView,UserDetailView
urlpatterns = [
  path('',UsersListView.as_view(),name='users'),
  path('create/',UserCreateView.as_view(),name='create-user'),
  path('<int:pk>',UserDetailView.as_view(),name='user-details' )
]
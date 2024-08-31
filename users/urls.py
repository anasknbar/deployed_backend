# from django.urls import path
# from .views import UserListView,UserDetailView,UserCreateView
# urlpatterns = [
#   path('',UserListView.as_view(),name='tenants'),
#   path('create',UserDetailView.as_view(),name='create_user'),
#   path('<int:pk>',UserCreateView.as_view(),name='user_details' )
# ]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]

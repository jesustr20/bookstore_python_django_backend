from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    UserCreateView, 
    UserListView,
    UserDetailView)

urlpatterns = [
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/list/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/detail',UserDetailView.as_view(), name='user-detail'),    
]
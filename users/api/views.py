from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from users.models import User
from users.api.serializers import (
    UserSerializer,
    UserListSerializer,
    UserDetailSerializer
    )
from users.api.services import UserService

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)        
        UserService.create_user(serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)        

class UserListView(generics.ListAPIView):    
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserService.get_all_users()

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.none()

    def get_object(self):
        if getattr(self, 'swagger_fake_view', False):
            return None
        return UserService.get_user(self.kwargs['pk'])
    
    def perform_update(self, serializer):
        UserService.update_user(self.kwargs['pk'], serializer.validated_data)

    def perform_destroy(self, instance):
        UserService.delete_user(self.kwargs['pk'])
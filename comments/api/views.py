from rest_framework import generics, serializers
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.exceptions import NotFound
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from comments.models import Comment
from comments.api.serializers import(
    CommentSerializer,
    CommentDetailSerializer,
    CommentListSerializer
    )
from comments.api.services import CommentService

class BaseCommentView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get_service(self):
        return CommentService(self.request.user)
    
    def get_permissions(self):
        if self.request.method in ["GET"]:
            return [AllowAny()]
        return [IsAuthenticated()]
    
    def get_comment_of_404(self, comment_id):
        service = self.get_service()
        try:
            return service.get_comment(comment_id)
        except NotFound:
            return NotFound("Comment not found")

class CommentCreateView(BaseCommentView, generics.CreateAPIView):
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        comment_service = self.get_service()
        comment_service.create_comment(serializer.validated_data)

class CommentListView(BaseCommentView, generics.ListAPIView):    
    serializer_class = CommentListSerializer    

    def get_queryset(self):        
        return Comment.objects.all()

class CommentDetailView(BaseCommentView, generics.RetrieveUpdateDestroyAPIView):    
    serializer_class = CommentDetailSerializer    

    def get_queryset(self):
        return Comment.objects.none()

    def get_object(self):
        try:
            return self.get_service().get_comment(self.kwargs['pk'])
        except ObjectDoesNotExist:
            raise NotFound("Comment not found")

    def perform_update(self, serializer):
        comment_service = self.get_service()
        comment_service.update_comment(self.kwargs['pk'], serializer.validated_data)
    
    def perform_destroy(self, instance):
        comment_service = self.get_service()
        comment_service.delete_comment(self.kwargs['pk'])
 
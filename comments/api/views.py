from rest_framework import generics, serializers
from rest_framework.permissions import IsAuthenticated,AllowAny
from comments.models import Comment
from comments.api.serializers import(
    CommentSerializer,
    CommentDetailSerializer,
    CommentListSerializer
    )
from comments.api.services import CommentService

class CommentView(generics.CreateAPIView):    
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        comment_data = serializer.validated_data
        comment_service = CommentService(self.request.user)
        comment_service.create_comment(comment_data)

class CommentListView(generics.ListAPIView):    
    serializer_class = CommentListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):        
        return Comment.objects.all()

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):    
    serializer_class = CommentDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.none()

    def get_object(self):
        comment_id = self.kwargs['pk']
        comment_service = CommentService(self.request.user)
        return comment_service.get_comment(comment_id)

    def perform_update(self, serializer):
        comment_service = CommentService(self.request.user)
        comment_service.update_comment(self.kwargs['pk'], serializer.validated_data)
    
    def perform_destroy(self, instance):
        comment_service = CommentService(self.request.user)
        comment_service.delete_comment(self.kwargs['pk'])
        
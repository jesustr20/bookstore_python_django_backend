from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import NotFound
from videos.models import Video
from videos.api.serializers import(
    VideoSerializer,
    VideoDetailSerializer,
    VideoListSerializer
)

from videos.api.services import VideoService

class BaseVideoView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get_service(self):
        return VideoService(self.request.user)
    
    def get_permissions(self):
        if self.request.method in ['GET']:
            return [AllowAny()]
        return [IsAuthenticated()]
    
    def get_video_of_404(self, video_id):
        service = self.get_service()
        try:
            return service.get_video(video_id)
        except NotFound:
            raise NotFound("Video not found")

class VideoCreateView(BaseVideoView, generics.CreateAPIView):    
    serializer_class = VideoSerializer
    
    def perform_create(self, serializer):
        video_serializer = self.get_service()
        video_serializer.create_video(serializer.validated_data)

class VideolListView(BaseVideoView, generics.ListAPIView):
    serializer_class = VideoListSerializer

    def get_queryset(self):
        return self.get_service().list_videos()
    

class VideolDetailView(BaseVideoView, generics.RetrieveUpdateDestroyAPIView):    
    serializer_class = VideoDetailSerializer
    
    def get_queryset(self):
        return Video.objects.none()
    
    def get_object(self):
        return self.get_service().get_video(self.kwargs['pk'])
    
    def perform_destroy(self, video_id):
        video_service = self.get_service()
        video_service.delete_video(video_id)
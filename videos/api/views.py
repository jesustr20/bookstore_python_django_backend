from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from videos.models import Video
from videos.api.serializers import(
    VideoSerializer,
    VideoDetailSerializer,
    VideoListSerializer
)

class VideoCreateView(generics.CreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [IsAuthenticated]

class VideolListView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoListSerializer
    permission_classes = [IsAuthenticated]

class VideolDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoDetailSerializer
    permission_classes = [IsAuthenticated]
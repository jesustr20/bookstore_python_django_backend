from django.core.exceptions import PermissionDenied
from videos.api.repositories import VideoRepository
from django.http import Http404

class VideoService:

    def __init__(self, user):
        self.user = user

    def list_videos(self):
        if self.user and self.user.is_staff:
            return VideoRepository.get_all_videos(self.user)
        raise PermissionDenied("You don't have permissions for views this videos list")
    
    def get_video(self, video_id):
        video = VideoRepository.get_video_by_id(video_id)
        if self.user and self.user.is_staff:
            if not video or (not video.is_active and not self.user.is_staff):
                raise Http404("Video not found or inactive")
            return video
        raise PermissionDenied("You don't have permissions for views this video list")
    
    def create_video(self, video_data):
        return VideoRepository.create_video(video_data, self.user)
    
    def delete_video(self, video_id):
        video = self.get_video(video_id)
        VideoRepository.delete_video(video)
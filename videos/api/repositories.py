from videos.models import Video

class VideoRepository:
    
    @staticmethod
    def get_all_videos(user):
        if user or user.is_staff:
            return Video.objects.filter(user=user)
        
    @staticmethod
    def get_video_for_user(user):
        return Video.objects.filter(user=user)
    
    @staticmethod
    def get_video_by_id(video_id):
        return Video.objects.filter(id=video_id).first()
    
    @staticmethod
    def create_video(video_data, user):
        if 'user' in video_data:
            del video_data['user']
        return Video.objects.create(**video_data, user=user)
    
    @staticmethod
    def delete_video(video):
        video.deactivate()
from rest_framework import serializers
from videos.models import Video
from comments.api.serializers import(
    CommentListSerializer,
    CommentDetailSerializer,
)

class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = '__all__'

class VideoListSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()
    comments = CommentListSerializer(many=True, read_only=True)
    
    class Meta:
        model = Video
        fields = ['id', 'title', 'author','published_date','user','comments']
    
    def get_user(self, obj):
        from users.api.serializers import UserListSerializer
        return UserListSerializer(obj.user).data

class VideoDetailSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()
    comments = CommentDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Video
        fields = ['id', 'title', 'author','published_date','user','comments']

    def get_user(self, obj):
        from users.api.serializers import UserDetailSerializer
        return UserDetailSerializer(obj.user).data
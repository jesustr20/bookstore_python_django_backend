from rest_framework import serializers
from documentals.models import Documental
from comments.api.serializers import(
    CommentListSerializer,
    CommentDetailSerializer,
)

class DocumentalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Documental
        fields = '__all__'

class DocumentalListSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()
    comments = CommentListSerializer(many=True, read_only=True)
    
    class Meta:
        model = Documental
        fields = ['id', 'title', 'author','published_date','user','comments']
    
    def get_user(self, obj):
        from users.api.serializers import UserListSerializer
        return UserListSerializer(obj.user).data

class DocumentalDetailSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()
    comments = CommentDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Documental
        fields = ['id', 'title', 'author','published_date','user','comments']

    def get_user(self, obj):
        from users.api.serializers import UserDetailSerializer
        return UserDetailSerializer(obj.user).data
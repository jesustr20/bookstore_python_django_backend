from rest_framework import serializers
from articles.models import Article
from comments.api.serializers import(
    CommentListSerializer,
    CommentDetailSerializer
)

class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'

class ArticleListSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()
    comments = CommentListSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'author','published_date','user','comments']
    
    def get_user(self, obj):
        from users.api.serializers import UserListSerializer
        return UserListSerializer(obj.user).data

class ArticleDetailSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    comments = CommentDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'author','published_date','user','comments']
    
    def get_user(self, obj):
        from users.api.serializers import UserDetailSerializer
        return UserDetailSerializer(obj.user).data


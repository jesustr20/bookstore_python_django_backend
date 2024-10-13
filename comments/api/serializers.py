from rest_framework import serializers
from comments.models import Comment
from django.contrib.contenttypes.models import ContentType

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'

class CommentListSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    content_object = serializers.SerializerMethodField()
    content_type = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id','user', 'content', 'score', 'created_at', 'content_type', 'object_id', 'content_object']
    
    def get_user(self, obj):
        from users.api.serializers import UserListSerializer
        return UserListSerializer(obj.user).data
    
    def get_content_type(self, obj):
        return obj.content_type.model

    def get_content_object(self, obj):
        content_object = obj.content_object

        if content_object is None:
            return None
        
        from users.models import User
        from books.models import Book
        from articles.models import Article
        from documentals.models import Documental
        from videos.models import Video

        if isinstance(content_object, User):            
            from users.api.serializers import UserListSerializer
            return UserListSerializer(content_object).data
        elif isinstance(content_object, Book):
            from books.api.serializers import BookListSerializer
            return BookListSerializer(content_object).data
        elif isinstance(content_object, Article):
            from articles.api.serializers import ArticleListSerializer
            return ArticleListSerializer(content_object).data
        elif isinstance(content_object, Documental):
            from documentals.api.serializers import DocumentalListSerializer
            return DocumentalListSerializer(content_object).data
        elif isinstance(content_object, Video):
            from videos.api.serializers import VideoListSerializer
            return VideoListSerializer(content_object).data
        else:
            return None

class CommentDetailSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    content_object = serializers.SerializerMethodField()
    content_type = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id','user', 'content', 'score', 'created_at', 'content_type', 'object_id', 'content_object']

    def get_user(self, obj):
        from users.api.serializers import UserDetailSerializer
        return UserDetailSerializer(obj.user).data
    
    def get_content_type(self, obj):
        return obj.content_type.model

    def get_content_object(self, obj):
        content_object = obj.content_object
        
        from users.models import User
        from books.models import Book
        from articles.models import Article
        from documentals.models import Documental
        from videos.models import Video

        if isinstance(content_object, User):
            from users.api.serializers import UserDetailSerializer            
            return UserDetailSerializer(content_object).data
        elif isinstance(content_object, Book):
            from books.api.serializers import BookDetailSerializer
            return BookDetailSerializer(content_object).data
        elif isinstance(content_object, Article):
            from articles.api.serializers import ArticleDetailSerializer
            return ArticleDetailSerializer(content_object).data
        elif isinstance(content_object, Documental):
            from documentals.api.serializers import DocumentalDetailSerializer
            return DocumentalDetailSerializer(content_object).data
        elif isinstance(content_object, Video):
            from videos.api.serializers import VideoDetailSerializer
            return VideoDetailSerializer(content_object).data
        else:
            return None
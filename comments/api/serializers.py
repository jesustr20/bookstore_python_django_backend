from rest_framework import serializers
from comments.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ['id','book','content','created_at']

class CommentListSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    book = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ['id','content','created_at','user','book']
    
    def get_user(self, obj):
        from users.api.serializers import UserListSerializer
        return UserListSerializer(obj.user).data

    def get_book(self, obj):
        from books.api.serializers import BookListSerializer
        return BookListSerializer(obj.book).data

class CommentDetailSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    book = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ['id','content','created_at','user','book']
    
    def get_user(self, obj):
        from users.api.serializers import UserDetailSerializer
        return UserDetailSerializer(obj.user).data

    def get_book(self, obj):
        from books.api.serializers import BookDetailSerializer
        return BookDetailSerializer(obj.book).data
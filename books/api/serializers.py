from rest_framework import serializers
from books.models import Book
from comments.api.serializers import(
    CommentListSerializer,
    CommentDetailSerializer
)

class BookSerializer(serializers.ModelSerializer):    
    user = serializers.StringRelatedField()
    comments = CommentListSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['id','title','author','published_date','privacy', 'user', 'comments']
    
    def get_user(self, obj):
        from users.api.serializers import UserListSerializer
        return UserListSerializer(obj.user).data

class BookListSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    comments = CommentListSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author','published_date','privacy','user','comments' ]

    def get_user(self, obj):
        from users.api.serializers import UserListSerializer
        return UserListSerializer(obj.user).data
    
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Book.objects.all()
        else:
            return Book.objects.filter(user=user)

class BookDetailSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    comments = CommentDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author','published_date','privacy','user','comments']
    
    def get_user(self, obj):
        from users.api.serializers import UserDetailSerializer
        return UserDetailSerializer(obj.user).data
    
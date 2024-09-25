from rest_framework import serializers
from users.models import User
from books.api.serializers import(
    BookListSerializer,
    BookDetailSerializer
)
from comments.api.serializers import(
    CommentListSerializer,
    CommentDetailSerializer
)

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name','password']
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class UserListSerializer(serializers.ModelSerializer):
    books = BookListSerializer(many=True, read_only=True)
    comments = CommentListSerializer(many=True, read_only=True)    

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name','password','last_name','is_active','is_staff','books','comments']

class UserDetailSerializer(serializers.ModelSerializer):
    books = BookDetailSerializer(many=True, read_only=True)
    comments = CommentDetailSerializer(many=True, read_only=True)
    new_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'books','comments','new_password']
    
    def update(self, instance, validated_data):
        new_password = validated_data.pop('new_password', None)
        super().update(instance, validated_data)

        if new_password:
            instance.set_password(new_password)
            instance.save()
        return instance
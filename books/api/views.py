from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from books.models import Book
from books.api.serializers import (
    BookSerializer,
    BookDetailSerializer,
    BookListSerializer
    )
from books.api.services import BookService

class BookCreateView(generics.CreateAPIView):    
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if getattr(self, 'swagger_fake_view', False):
            return
        book_data = serializer.validated_data
        book_service = BookService(self.request.user)
        book_service.create_book(book_data)

class BookListView(generics.ListAPIView):    
    serializer_class = BookListSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return[AllowAny()]
        return [IsAuthenticated()]

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.is_staff:
            return Book.objects.all()
        return Book.objects.filter(privacy='public')

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):    
    serializer_class = BookDetailSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.is_staff:
            return Book.objects.all()
        return Book.objects.filter(privacy='public')
    
    def get_object(self):
        book_id = self.kwargs['pk']
        book_service = BookService(self.request.user)
        book = book_service.get_book(book_id)
        
        return book
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import NotFound
from django_filters.rest_framework import DjangoFilterBackend
from books.api.filters import BookFilter
from django.http import Http404
from books.models import Book
from books.api.serializers import (
    BookSerializer,
    BookDetailSerializer,
    BookListSerializer
    )
from books.api.services import BookService

class BaseBookView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]
    
    def get_service(self):
        swagger_fake_view = getattr(self, 'swagger_fake_view', False)
        return BookService(user=self.request.user, swagger_fake_view=swagger_fake_view)
    
    def get_object_or_404(self, book_id):
        return self.get_service().get_book(book_id)

class BookCreateView(BaseBookView, generics.CreateAPIView):    
    serializer_class = BookSerializer    

    def perform_create(self, serializer):
        book_service = self.get_service()
        book_service.create_book(serializer.validated_data)


class BookListView(BaseBookView, generics.ListAPIView):
    serializer_class = BookListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.is_staff: 
            return Book.objects.all()
        return Book.objects.filter(privacy='public', is_active=True)


class BookDetailView(BaseBookView, generics.RetrieveUpdateDestroyAPIView):    
    serializer_class = BookDetailSerializer

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Book.objects.none()
        
        
        if self.request.user.is_authenticated and self.request.user.is_staff:
            return Book.objects.all()
        return Book.objects.filter(privacy='public', is_active=True)
    
    
    def get_object(self):
        book_id = self.kwargs['pk']
        book_service = self.get_service()

        try:
            book = book_service.get_book(book_id)
        except Http404:
            raise NotFound("Book not found.")
        return book
    
    def perform_destroy(self, book_id):
        book_service = self.get_service()
        book_service.delete_book(book_id)

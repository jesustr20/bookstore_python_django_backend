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

        book_service = self.get_service()
        books_data = book_service.list_books()

        #print(books_data)

        # Imprime el tipo y contenido de books_data para inspección
        #print("Tipo de books_data:", type(books_data))
        #print("Contenido de books_data:", books_data)

        # Dependiendo de lo que imprima, ajustamos cómo acceder al 'id'
        #if isinstance(books_data, list):
        #    # Si books_data es una lista, vamos a verificar qué contiene cada elemento
        #    print("Primer elemento de books_data:", books_data[0] if books_data else "Lista vacía")

        # Suponiendo que books_data sea una lista de objetos o diccionarios
        # Intentamos acceder a los ids según el tipo de elemento

        # Caso 1: Si es una lista de diccionarios
        #if isinstance(books_data, list) and isinstance(books_data[0], dict):
        #    book_ids = [book.get('id') for book in books_data]
        #    print("ID: ",book_ids)
        ## Caso 2: Si es una lista de objetos, como un modelo Book
        #elif isinstance(books_data, list) and hasattr(books_data[0], dict):
        #    book_ids = [book.get('id') for book in books_data]
        #    print("ID: ",book_ids)
        #else:
        #    book_ids = []

        print("book_ids:", books_data)

        #return Book.objects.filter(id__in=[book_ids.get('id') for book ])
        if self.request.user.is_authenticated and self.request.user.is_staff: 
            return Book.objects.all().order_by('id')
        return Book.objects.filter(privacy='public', is_active=True).order_by('id')


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

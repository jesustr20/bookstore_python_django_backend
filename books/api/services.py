from django.core.exceptions import PermissionDenied
from books.api.repositories import BookRepository
from django.http import Http404
from django.core.cache import cache
import json
from .serializers import BookSerializer 

class BookService:

    def __init__(self, user=None, swagger_fake_view=False) -> None:
        self.user=user

        if user and user.is_anonymous and not swagger_fake_view:
            self.user = None
    def _get_cache_key(self, book_id):
        return f"book_{book_id}"

    def list_books(self):
        cache_key = f"books_list_user_{self.user.id if self.user else 'anonymous'}"
        print(f"Cache set for key: {cache_key}")
        cached_books = cache.get(cache_key)
    
        if cached_books:
            print("Redis Cache Hit: List Books")
            return json.loads(cached_books)
    
        print("Redis Cache Miss, Consulting to the DB: List Books")
        if self.user and self.user.is_staff:
            books = BookRepository.get_all_books(self.user)
            print('LISTA DE BOOKS: ',books)
        elif self.user and self.user.is_authenticated:
            books = BookRepository.get_books_by_user(self.user)
            print('LISTA DE BOOKS: ',books)
        else:
            books = BookRepository.get_all_books(None)
            print('LISTA DE BOOKS: ',books)
    
        serializer = BookSerializer(books, many=True)
        books_data = json.dumps(serializer.data)

        print('SERIALIZADA: ',serializer.data)
        print(f"Cache key generated: {cache_key}")
        print(f"Data stored in Redis: {books_data}")
    
        cache.set(cache_key, books_data, timeout=3600)
        return serializer.data

    def get_book(self, book_id):
        cache_key = self._get_cache_key(book_id)

        # Intentamos obtener el libro desde Redis
        cached_book = cache.get(cache_key)
        if cached_book:
            print("Redis Cache Hit")
            return json.loads(cached_book)  # Convertimos el JSON almacenado de vuelta a un diccionario
        
        print("Redis Cache Miss, Consulting to the DB")
        
        # Obtenemos el libro desde la base de datos
        book = BookRepository.get_book_by_id(self.user, book_id)
        if book is None:
            raise Http404("Book not found")

        # Serializamos el libro antes de almacenarlo en Redis
        serializer = BookSerializer(book)  # Usamos el serializador para convertir el modelo en datos JSON
        book_data = json.dumps(serializer.data)  # Convertimos el resultado a JSON
        print("Serialized data before storing in Redis:", book_data)
        # Almacenamos el libro serializado en Redis
        cache.set(cache_key, book_data, timeout=3600)
        return serializer.data
    
    def create_book(self, book_data):
        book = BookRepository.create_book(book_data, self.user)

        serializer = BookSerializer(book)
        book_data = json.dumps(serializer.data)

        cache_key = self._get_cache_key(book.id)
        cache.set(cache_key, book_data, timeout=3600)
        return serializer.data
    
    def delete_book(self, book):
        cache_key = self._get_cache_key(book.id)
        cache.delete(cache_key)
        BookRepository.delete_book(book)
from django.core.exceptions import PermissionDenied
from books.models import Book
from django.db import models

class BookRepository:
    
    @staticmethod
    def get_all_books(user):
        if user and user.is_staff:
            return Book.objects.all()
        if user and user.is_authenticated:
            return Book.objects.filter(
                models.Q(privacy='public') |
                models.Q(privacy='authenticated') |
                models.Q(user=user)
            )
        return Book.objects.filter(privacy='public')
    
    @staticmethod
    def get_books_by_user(user):
        return Book.objects.filter(user=user)
    
    @staticmethod
    def get_book_by_id(user, book_id):
        book = Book.objects.filter(id=book_id).first()

        if not book:
            return None
    
        if book.privacy == 'public':
            return book
        
        if book.privacy in ['authenticated', 'private']:
            if not user or user.is_anonymous:
                raise PermissionDenied("Debes estar autenticado para ver este libro.")
            
            if book.privacy == 'private' and book.user != user:
                raise PermissionDenied("No tienes permiso para ver este libro.")
        
        return book

    @staticmethod
    def create_book(book_data, user):
        if 'user' in book_data:
            del book_data['user']
        return Book.objects.create(**book_data, user=user)
    
    @staticmethod
    def delete_book(book):
        book.is_active = False
        book.save()
from django.core.exceptions import PermissionDenied
from books.api.repositories import BookRepository
from django.http import Http404

class BookService:

    def __init__(self, user=None, swagger_fake_view=False) -> None:
        self.user=user

        if user and user.is_anonymous and not swagger_fake_view:
            self.user = None
        

    def list_books(self):
        if self.user and self.user.is_staff:
            return BookRepository.get_all_books(self.user)
        if self.user and self.user.is_authenticated:
            return BookRepository.get_books_by_user(self.user)
        return BookRepository.get_all_books(None)

    def get_book(self, book_id):
        book = BookRepository.get_book_by_id(self.user, book_id)
        if book is None:
            raise Http404("Book not found")
        return book
    
    def create_book(self, book_data):
        return BookRepository.create_book(book_data, self.user)
    
    def delete_book(self, book):
        return BookRepository.delete_book(book)
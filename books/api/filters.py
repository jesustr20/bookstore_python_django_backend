import django_filters
from books.models import Book

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'privacy']
from django.urls import path
from books.api.views import (
    BookCreateView,
    BookListView, 
    BookDetailView)

urlpatterns = [
    path('create/', BookCreateView.as_view(), name='book-create'),
    path('list/', BookListView.as_view(), name='book-list'),
    path('<int:pk>/', BookDetailView.as_view(), name='book-detail')
]
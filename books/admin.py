from django.contrib import admin
from books.models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author','published_date','user', 'privacy','get_comment_count','is_active']

    def get_comment_count(self, obj):
        return obj.comment.count()
    get_comment_count.short_description = 'Comment Count'

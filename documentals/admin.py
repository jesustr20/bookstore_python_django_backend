from django.contrib import admin
from documentals.models import Documental

# Register your models here.
@admin.register(Documental)
class DocumentalAdmin(admin.ModelAdmin):
    list_display = ['title', 'author','published_date','user', 'get_comment_count']

    def get_comment_count(self, obj):
        return obj.comment.count()
    get_comment_count.short_description = 'Comment Count'
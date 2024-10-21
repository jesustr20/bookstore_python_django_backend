from django.contrib import admin
from comments.models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'score', 'created_at', 'user', 'content_type', 'object_id', 'content_object', 'is_active']

    # Método para mostrar la cantidad de objetos relacionados con el 'content_type'
    def related_object_count(self, obj):
        model_class = obj.content_type.model_class()
        if model_class:
            return model_class.objects.count()
        return "N/A"
    
    related_object_count.short_description = "Total Objects"

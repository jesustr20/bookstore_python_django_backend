from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from comments.models import Comment
from django.apps import apps

@receiver(post_save)
def deactivate_comments_on_instance_inactive(sender, instance, **kwargs):
    if hasattr(instance, 'is_active') and not instance.is_active:
        content_type = ContentType.objects.get_for_model(sender)
        Comment.objects.filter(content_type=content_type, 
                               object_id = instance.id).update(is_active=False)
        
def connect_signals():
    models_to_connect = ['books.Book', 'videos.Video', 'articles.Article', 'documentals.Documental']
    for model_path in models_to_connect:
        model = apps.get_model(model_path)
        post_save.connect(
            deactivate_comments_on_instance_inactive,
            sender=model,
            dispatch_uid=r'deactivate_comments_{model.__name__}'
        )
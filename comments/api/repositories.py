from comments.models import Comment
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q

class CommentRepository:

    @staticmethod
    def get_comment_by_id(comment_id):
        return Comment.objects.filter(id=comment_id, is_active=True).first()
    
    @staticmethod
    def get_comments_for_instance(instance, show_inactive=False):
        content_type = ContentType.objects.get_for_model(instance)
        query = Comment.objects.filter(content_type=content_type, object_id=instance.id)
        if not show_inactive:
            query=query.filter(is_active=True)
        return query

    @staticmethod
    def create_comment(instance, comment_data, user):
        content_type = ContentType.objects.get_for_model(instance)
        comment_data.pop('user', 'none')
        return Comment.objects.create(
            content_type=content_type,
            object_id=instance.id,
            user=user,
            **comment_data
        )

    @staticmethod
    def update_comment(comment, comment_data):
        for key, value in comment_data.items():
            setattr(comment, key, value)
        comment.save()
        return comment
    
    @staticmethod
    def delete_comment(comment):
        comment.deactivate()
    
    @staticmethod
    def get_comment_for_user(user, show_inactive=False):
        query = Comment.objects.filter(user=user)
        if not show_inactive:
            query = query.filter(is_active=True)
        return query
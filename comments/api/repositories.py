from comments.models import Comment
from django.db.models import Q

class CommentRepository:

    @staticmethod
    def get_comment_by_id(comment_id):
        return Comment.objects.filter(id=comment_id).first()
    
    @staticmethod
    def get_comments_for_book(book_id):
        return Comment.objects.filter(book__id=book_id)

    @staticmethod
    def create_comment(comment_data, user):
        comment_data.pop('user', None)
        return Comment.objects.create(**comment_data, user=user)
    
    @staticmethod
    def update_comment(comment, comment_data):
        for key, value in comment_data.items():
            setattr(comment, key, value)
        comment.save()
        return comment
    
    @staticmethod
    def delete_comment(comment):
        comment.delete()
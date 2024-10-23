from comments.api.repositories import CommentRepository
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist

class CommentService:

    def __init__(self, user):
        self.user = user

    def create_comment(self, instance, comment_data):

        if not self.user.is_authenticated:
            raise PermissionDenied("Use must be authenticated")
        return CommentRepository.create_comment(instance, comment_data, self.user)
    
    def get_comment(self, comment_id):
        comment = CommentRepository.get_comment_by_id(comment_id)
        if not comment:
            raise ObjectDoesNotExist("Comment not found")
        if not comment.is_active and not self.user.is_staff:
            raise PermissionDenied("You do not have permission to view this comment")
        return comment
    
    def get_comments_for_instance(self, instance):
        show_inactive=self.user.is_staff
        return CommentRepository.get_comments_for_instance(instance, show_inactive)
    
    def update_comment(self, comment_id, comment_data):
        comment = self.get_comment(comment_id)
        if comment.user != self.user and not self.user.is_staff:
            raise PermissionDenied("You do not have permission to edit this comment")
        return CommentRepository.update_comment(comment, comment_data)
    
    def delete_comment(self, comment_id):
        comment = self.get_comment(comment_id)
        if comment.user != self.user and not self.user.is_staff:
            raise PermissionDenied("You do not have perission to edit this comment")
        CommentRepository.delete_comment(comment)
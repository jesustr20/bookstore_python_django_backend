from comments.api.repositories import CommentRepository
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist

class CommentService:

    def __init__(self, user):
        self.user = user

    def create_comment(self, comment_data):

        if not self.user.is_authenticated:
            raise PermissionDenied("Use must be authenticated")
        return CommentRepository.create_comment(comment_data, self.user)
    
    def get_comment(self, comment_id):
        comment = CommentRepository.get_comment_by_id(comment_id)
        if not comment:
            raise ObjectDoesNotExist("Comment not found")
        return comment
    
    def get_comments_for_book(self, book_id):
        return CommentRepository.get_comments_for_book(book_id)
    
    def update_comment(self, comment_id, comment_data):
        comment = self.get_comment(comment_id)
        if comment.user != self.user:
            raise PermissionDenied("You do not have permission to edit this comment")
        return CommentRepository.update_comment(comment, comment_data)
    
    def delete_comment(self, comment_id):
        comment = self.get_comment(comment_id)
        if comment.user != self.user:
            raise PermissionDenied("You do not have perission to edit this comment")
        return CommentRepository.delete_comment(comment)
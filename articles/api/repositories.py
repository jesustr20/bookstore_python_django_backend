from django.core.exceptions import PermissionDenied
from articles.models import Article
from django.db.models import Q

class ArticleRepository:

    @staticmethod
    def get_all_articles(user):
        if user or user.is_staff:
            return Article.objects.all()        
    
    @staticmethod
    def get_article_for_user(user):
        return Article.objects.filter(user=user)

    @staticmethod
    def get_article_by_id(article_id):
        return Article.objects.filter(id=article_id).first()        
        
    @staticmethod
    def create_article(article_data, user):
        if 'user' in article_data:
            del article_data['user']
        return Article.objects.create(**article_data, user=user)
    
    @staticmethod
    def delete_article(article):
        article.deactivate()
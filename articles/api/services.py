from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from articles.api.repositories import ArticleRepository
from django.http import Http404

class ArticleService:
    
    def __init__(self, user):
        self.user = user

    def list_articles(self):
        if self.user and self.user.is_staff:
            return ArticleRepository.get_all_articles(self.user)
        raise PermissionDenied("No tienes permiso para ver la lista de articulos.")
    
    def get_article(self, article_id):
        article = ArticleRepository.get_article_by_id(article_id)
        if self.user and self.user.is_staff:
            if not article or (not article.is_active and not self.user.is_staff):
                raise Http404("Article not found or inactive")
            return article
        raise PermissionDenied("No tienes permiso para ver la lista de articulos.")
    
    def create_article(self, article_data):        
        return ArticleRepository.create_article(article_data, self.user)        

    def delete_article(self, article_id):
        article = self.get_article(article_id)
        ArticleRepository.delete_article(article)
    

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import NotFound
from django.core.exceptions import ObjectDoesNotExist
from articles.models import Article
from articles.api.serializers import (
    ArticleSerializer,
    ArticleDetailSerializer,
    ArticleListSerializer,
)
from articles.api.services import ArticleService

class BaseArticleView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get_service(self):
        return ArticleService(self.request.user)
    
    def get_permissions(self):
        if self.request.method in ['GET']:
            return [AllowAny()]
        return [IsAuthenticated()]
    
    def get_article_of_404(self, article_id):
        service = self.get_service()
        try:
            return service.get_article(article_id)
        except NotFound:
            raise NotFound("Article not found")

class ArticleCreateView(BaseArticleView, generics.CreateAPIView):
    serializer_class = ArticleSerializer
    
    def perform_create(self, serializer):
        article_serializer = self.get_service()
        article_serializer.create_article(serializer.validated_data)

class ArticleListView(BaseArticleView, generics.ListAPIView):
    serializer_class = ArticleListSerializer
    
    def get_queryset(self):        
        return self.get_service().list_articles()

class ArticleDetailView(BaseArticleView, generics.RetrieveUpdateDestroyAPIView):    
    serializer_class = ArticleDetailSerializer
    
    def get_queryset(self):
        return Article.objects.none()
    
    def get_object(self):
        return self.get_service().get_article(self.kwargs['pk'])        
        
    def perform_destroy(self, article_id):
        article_service = self.get_service()
        article_service.delete_article(article_id)

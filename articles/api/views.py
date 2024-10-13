from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from articles.models import Article
from articles.api.serializers import (
    ArticleSerializer,
    ArticleDetailSerializer,
    ArticleListSerializer,
)

class ArticleCreateView(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    permission_classes = [IsAuthenticated]

class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    permission_classes = [IsAuthenticated]

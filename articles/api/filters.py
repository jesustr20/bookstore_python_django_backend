import django_filters
from articles.models import Article

class ArticleFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Article
        fields = ['title', 'author', 'published_date']
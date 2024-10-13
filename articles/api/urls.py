from django.urls import path
from articles.api.views import(
    ArticleCreateView,
    ArticleListView,
    ArticleDetailView,
)

urlpatterns = [
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('list/', ArticleListView.as_view(), name='article-list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article-detail')
]
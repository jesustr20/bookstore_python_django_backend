from django.urls import path
from comments.api.views import (
    CommentCreateView, 
    CommentListView,
    CommentDetailView,
    )

urlpatterns = [
    path('create/', CommentCreateView.as_view(), name='comment-create'),
    path('list/', CommentListView.as_view(), name='comment-list'),
    path('<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),    
]
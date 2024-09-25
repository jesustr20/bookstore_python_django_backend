from django.urls import path
from comments.api.views import (
    CommentView, 
    CommentListView,
    CommentDetailView
    )

urlpatterns = [
    path('create/', CommentView.as_view(), name='comment-create'),
    path('list/', CommentListView.as_view(), name='comment-list'),
    path('<int:pk>/', CommentDetailView.as_view(), name='comment-detail')
]
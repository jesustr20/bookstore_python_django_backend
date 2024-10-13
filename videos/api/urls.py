from django.urls import path
from videos.api.views import (
    VideoCreateView,
    VideolListView,
    VideolDetailView,
)

urlpatterns = [
    path('create/', VideoCreateView.as_view(), name='video-create'),
    path('list/', VideolListView.as_view(), name='video-list'),
    path('<int:pk>/', VideolDetailView.as_view(), name='video-detail')
]
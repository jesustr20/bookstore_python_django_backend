from django.urls import path
from documentals.api.views import (
    DocumentalCreateView,
    DocumentalListView,
    DocumentalDetailView,
)

urlpatterns = [
    path('create/', DocumentalCreateView.as_view(), name='documental-create'),
    path('list/', DocumentalListView.as_view(), name='documental-list'),
    path('<int:pk>/', DocumentalDetailView.as_view(), name='documental-detail')
]
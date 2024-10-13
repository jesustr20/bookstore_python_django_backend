from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from documentals.models import Documental
from documentals.api.serializers import(
    DocumentalSerializer,
    DocumentalDetailSerializer,
    DocumentalListSerializer
)

class DocumentalCreateView(generics.CreateAPIView):
    queryset = Documental.objects.all()
    serializer_class = DocumentalSerializer
    permission_classes = [IsAuthenticated]

class DocumentalListView(generics.ListAPIView):
    queryset = Documental.objects.all()
    serializer_class = DocumentalListSerializer
    permission_classes = [IsAuthenticated]

class DocumentalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Documental.objects.all()
    serializer_class = DocumentalDetailSerializer
    permission_classes = [IsAuthenticated]
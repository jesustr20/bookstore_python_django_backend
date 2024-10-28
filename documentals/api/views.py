from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import NotFound
from django_filters.rest_framework import DjangoFilterBackend
from documentals.api.filters import DocumentalFilter
from documentals.models import Documental
from documentals.api.serializers import(
    DocumentalSerializer,
    DocumentalDetailSerializer,
    DocumentalListSerializer
)

from documentals.api.services import DocumentalService

class BaseDocumentalView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get_service(self):
        return DocumentalService(self.request.user)
    
    def get_permissions(self):
        if self.request.method in ['GET']:
            return [AllowAny()]
        return [IsAuthenticated()]
    
    def get_documental_of_404(self, documental_id):
        service = self.get_service()
        try:
            return service.get_documental(documental_id)
        except NotFound:
            raise NotFound("Documental not found")

class DocumentalCreateView(BaseDocumentalView, generics.CreateAPIView):    
    serializer_class = DocumentalSerializer
    
    def perform_create(self, serializer):
        documental_serializer = self.get_service()
        documental_serializer.create_documental(serializer.validated_data)

class DocumentalListView(BaseDocumentalView, generics.ListAPIView):
    serializer_class = DocumentalListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = DocumentalFilter

    def get_queryset(self):
        return self.get_service().list_documentals()

class DocumentalDetailView(BaseDocumentalView, generics.RetrieveUpdateDestroyAPIView):    
    serializer_class = DocumentalDetailSerializer
    
    def get_queryset(self):
        return Documental.objects.none()
    
    def get_object(self):
        return self.get_service().get_documental(self.kwargs['pk'])
    
    def perform_destroy(self, documental_id):
        documental_service = self.get_service()
        documental_service.delete_documental(documental_id)
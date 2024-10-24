from django.core.exceptions import PermissionDenied
from documentals.api.repositories import DocumentalRepository
from django.http import Http404

class DocumentalService:

    def __init__(self, user):
        self.user = user
    
    def list_documentals(self):
        if self.user and self.user.is_staff:
            return DocumentalRepository.get_all_documentals(self.user)
        raise PermissionDenied("You don't have permissions for views this documentals list")
    
    def get_documental(self, documental_id):
        documental = DocumentalRepository.get_documental_by_id(documental_id)
        if self.user and self.user.is_staff:
            if not documental or (not documental.is_active and not self.user.is_staff):
                raise Http404("Documental not found or inactive")
            return documental
        raise PermissionDenied("You don't have permissions for views this documentals list")
    
    def create_documental(self, documental_data):
        return DocumentalRepository.create_documental(documental_data, self.user)
    
    def delete_documental(self, documental_id):
        documental = self.get_documental(documental_id)
        DocumentalRepository.delete_documental(documental)
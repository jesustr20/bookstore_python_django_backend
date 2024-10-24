from documentals.models import Documental

class DocumentalRepository:

    @staticmethod
    def get_all_documentals(user):
        if user or user.is_staff:
            return Documental.objects.all()
    
    @staticmethod
    def get_documental_for_user(user):
        return Documental.objects.filter(user=user)
    
    @staticmethod
    def get_documental_by_id(documental_id):
        return Documental.objects.filter(id=documental_id).first()
    
    @staticmethod
    def create_documental(documenta_data, user):
        if 'user' in documenta_data:
            del documenta_data['user']
        return Documental.objects.create(**documenta_data, user=user)
    
    @staticmethod
    def delete_documental(documental):
        documental.deactivate()

from django.db import models

class InspectableModel(models.Model):
    class Meta:
        abstract = True
    
    def inspect(self):
        attributes = [f"{field.name}: {field.get_internal_type().lower()}" for field in self._meta.get_fields()]
        return f"{self.__class__.__name__}({', '.join(attributes)})"
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from mixins import InspectableModel
from comments.models import Comment

# Create your models here.
User = get_user_model()

class Video(InspectableModel, models.Model):
    
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="videos")
    comment = GenericRelation(Comment)

    def __str__(self) -> str:
        return self.title
    
    def deactivate(self):
        self.is_active = False
        self.save()

from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Book(models.Model):
    PRIVACY_CHOICES = [
        ('public', 'Public (Anonymous users can see)'),
        ('authenticated', 'Authenticated users only'),
        ('private', 'Private (Only creator)'),
    ]

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="books")
    privacy = models.CharField(max_length=13, choices=PRIVACY_CHOICES, default='private')

    def __str__(self) -> str:
        return self.title
from django.db import models
import uuid


class Book(models.Model):
    name = models.CharField(max_length=300)
    author = models.CharField(max_length=300, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    category = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

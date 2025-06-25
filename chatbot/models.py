from django.db import models

# Create your models here.
from django.db import models

class Query(models.Model):
    text = models.CharField(max_length=255)
    response = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

from django.db import models

class ConsumerHelpDatabase(models.Model):
    query = models.CharField(max_length=255)
    response = models.TextField()

    def __str__(self):
        return self.query

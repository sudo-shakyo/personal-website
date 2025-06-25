from unittest.util import _MAX_LENGTH
from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User




# Create your models here.

#contact
class Contact(models.Model):
    name= models.CharField(max_length=1000)
    email=models.CharField(max_length=1000)
    username=models.CharField(max_length=1000)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name  
#message
class Msg(models.Model):
    name1=models.CharField(max_length=200)
    msg=models.TextField()
    date1=models.DateField()
    def __str__(self):
        return self.name1    
#search(not working)
class Search(models.Model):
    search=models.TextField()
    def __str__(self):
        return self.search




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

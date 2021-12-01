from enum import auto
from django.db import models
from uuid import uuid4

class Books (models.Model):
    id_books = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    relese_year = models.IntegerField()
    state= models.CharField(max_length=40)
    pages = models.IntegerField()
    publishing_company = models.CharField(max_length=100)
    create_at = models.DateField(auto_now_add=True)



    


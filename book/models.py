from django.db import models
from django.utils import timezone



class Book (models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    pub_date=models.DateTimeField()
    isbn_num=models.CharField(max_length=13)
    pages_amount=models.IntegerField()
    link=models.URLField(max_length=300)
    pub_language=models.CharField(max_length=30)

    def __str__(self):
        return self.title

# Create your models here.
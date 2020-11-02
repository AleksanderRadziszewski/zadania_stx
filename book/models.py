from django.db import models
from django.utils import timezone



class Book (models.Model):
    title=models.CharField(max_length=100,blank=True)
    author=models.CharField(max_length=100,blank=True)
    pub_date=models.CharField(max_length=30)
    isbn_num=models.CharField(max_length=30)
    pages_amount=models.IntegerField()
    link=models.URLField(max_length=300)
    pub_language=models.CharField(max_length=30)

    def __str__(self):
        return self.title

# Create your models here.

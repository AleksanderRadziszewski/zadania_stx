from django.db import models
from django.utils.text import slugify


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, default="Rowling")
    pub_date = models.CharField(max_length=30)
    isbn_num = models.CharField(max_length=13, unique=True)
    pages_amount = models.IntegerField()
    link = models.URLField(max_length=300)
    pub_language = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)




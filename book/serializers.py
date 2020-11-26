from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=["title", "author", "pub_date", "isbn_num", "pages_amount", "link", "pub_language"]



from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=["title", "author", "pub_date", "isbn_num", "pages_amount", "link", "pub_language"]




    # title = serializers.CharField(max_length=100, allow_blank=True)
    # author = serializers.CharField(max_length=100, allow_blank=True)
    # pub_date = serializers.CharField(max_length=30)
    # isbn_num = serializers.CharField(max_length=30)
    # pages_amount = serializers.IntegerField()
    # link = serializers.URLField(max_length=300)
    # pub_language = serializers.CharField(max_length=30)
    #
    # def create(self, validated_data):
    #     return Book.objects.create(validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.author = validated_data.get('author', instance.author)
    #     instance.pub_date = validated_data.get('pub_date', instance.pub_date)
    #     instance.isbn_num = validated_data.get('isbn_num', instance.isbn_num)
    #     instance.pages_amount = validated_data.get('pages_amount', instance.pages_amount)
    #     instance.link = validated_data.get('link', instance.link)
    #     instance.pub_language = validated_data.get('pub_language', instance.pub_language)


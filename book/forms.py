from datetime import date
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

from book.models import Book


class SearchForm(forms.Form):
    search_input=forms.CharField(max_length=50, required=False)
    pub_date_since=forms.CharField(help_text="yyyy", required=False)
    pub_date_to=forms.CharField(help_text="yyyy",required=False)

class SearchApiForm(forms.Form):
    search_input=forms.CharField(max_length=50)

class AddUpdateBookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=('title','author','isbn_num', 'pub_language', 'pages_amount', 'pub_date','link')
        validators={
            "link":URLValidator(schemes=['http']),

        }



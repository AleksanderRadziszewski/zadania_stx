from django.urls import path
from .views import book_list

from book import views

urlpatterns = [
    path("list_book/", book_list),
]
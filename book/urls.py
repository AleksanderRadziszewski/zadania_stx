from django.urls import path
from book import views

urlpatterns = [
    path("books_list/", views.books_list),
    path("book_detail/<int:pk>/", views.book_detail),
]
from django.urls import path
from book import views

urlpatterns = [
    path("books_list/", views.BookListCreateAPIView.as_view(), name="book api view"),
    path("book_detail/<int:id>/", views.BookDetailAPIView.as_view(), name="book details api view"),
    path("book_search_filter/<str:title>/", views.BookSearchFilterAPIView.as_view(), name="book search api view"),

]

from django.urls import path
from book import views

urlpatterns = [
    path("books_list/", views.BookAPIView.as_view(), name="book_api_view"),
    path("book_detail/<int:id>/", views.BookDetailsApiView.as_view(), name="book_details_api_view"),

]

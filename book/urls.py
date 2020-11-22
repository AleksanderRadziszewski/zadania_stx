from django.urls import path
from book import views

urlpatterns = [
    path("books_list/", views.GenericAPIView.as_view(), name="book_api_view"),
    path("book_detail/<int:id>/", views.GenericDetailAPIView.as_view(), name="book_details_api_view"),

]

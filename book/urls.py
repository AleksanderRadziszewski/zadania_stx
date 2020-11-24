from django.urls import path
from book import views

urlpatterns = [
    path("book_search_filter/<str:title>/", views.BookSearchFilterAPIView.as_view(), name="book search api view"),

]

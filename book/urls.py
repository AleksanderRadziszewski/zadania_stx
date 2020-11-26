from django.urls import path
from book import views

urlpatterns = [
    path("books_filter_search/<str:title>/", views.BookSearchFilterAPIView.as_view(), name="book search api view"),

]

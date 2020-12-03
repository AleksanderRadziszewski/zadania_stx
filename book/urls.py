from django.urls import path, include
from book import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("books", views.BookViewSet, basename="book")

urlpatterns = [
    path("books_filter_search/<str:title>/", views.BookSearchFilterAPIView.as_view(), name="book search api"),
    path("viewset/", include(router.urls)),
]

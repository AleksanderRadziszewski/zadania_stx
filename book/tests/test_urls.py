from django.test import SimpleTestCase
from django.urls import reverse, resolve, path, include
from django_api_client import status
from rest_framework.test import CoreAPIClient, APIClient, APITestCase, URLPatternsTestCase
from book import views


class TestUrls(SimpleTestCase):

    def test_search_book_list_url_is_resolve(self):
        url = reverse("search book list")
        self.assertEquals(resolve(url).func.view_class, views.SearchBookListView)

    def test_book_import_url_is_resolve(self):
        url = reverse("book import")
        self.assertEquals(resolve(url).func.view_class, views.BooksImportView)

    def test_book_update_url_is_resolve(self):
        url = reverse("update", kwargs={"pk": 522})
        self.assertEquals(resolve(url).func.view_class, views.AddUpdateBookView)

    def test_welcome_url_is_resolve(self):
        url = reverse("welcome")
        self.assertEquals(resolve(url).func.view_class, views.WelcomeView)

    def test_book_search_api_url_is_resolve(self):
        url = reverse("book search api", kwargs={"title": "King of the Alex"})
        self.assertEquals(resolve(url).func.view_class, views.BookSearchFilterAPIView)

class TestBookRestAPI(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('book', include('book.urls')),
    ]
    def test_create_book(self):
        url=reverse("book-list")
        response=self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)





from django.test import SimpleTestCase
from django.urls import reverse, resolve, path, include
from django_api_client import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from book import views
from book.models import Book



class TestUrls(SimpleTestCase):

    def test_book_list_url_is_resolve(self):
        url = reverse("search book list")
        self.assertEquals(resolve(url).func.view_class, views.BookListSearchView)

    def test_book_import_url_is_resolve(self):
        url = reverse("book import")
        self.assertEquals(resolve(url).func.view_class, views.BooksImportView)

    def test_book_add_url_is_resolve(self):
        url = reverse("add")
        self.assertEquals(resolve(url).func.view_class, views.BookAddView)

    def test_book_update_url_is_resolve(self):
        url = reverse("update", kwargs={"pk": 522})
        self.assertEquals(resolve(url).func.view_class, views.BookUpdateView)

    def test_welcome_url_is_resolve(self):
        url = reverse("welcome")
        self.assertEquals(resolve(url).func.view_class, views.WelcomeView)

    def test_book_search_api_url_is_resolve(self):
        url = reverse("book search api", kwargs={"title": "King of the Alex"})
        self.assertEquals(resolve(url).func.view_class, views.BookSearchFilterAPIView)





class TestBookRestAPI(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('books_rest/', include('book.urls')),
    ]

    def setUp(self):
        self.url_add = reverse("book-list")

        self.data_set_up = Book.objects.create(
            title="Rest Api Test",
            author="me",
            pub_date="2020",
            isbn_num="9781426749490",
            pages_amount=666,
            pub_language="EN",
            link="http://www.google.pl"
        )

        self.url_edit = f"/books_rest/viewset/books/{self.data_set_up.id}/"

    def test_book_create_rest_url(self):
        response = self.client.get(self.url_add)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_book_delete_put_rest_url(self):
        response = self.client.get(self.url_edit)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_book_delete_put_rest_url_not_exist(self):
        self.url_edit_not_exist=self.url_edit = f"/books_rest/viewset/books/666/"
        response = self.client.get(self.url_edit_not_exist
                                   )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

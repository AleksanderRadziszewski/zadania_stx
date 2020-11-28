from django.test import SimpleTestCase
from django.urls import reverse, resolve, reverse_lazy
from book import views
from book.urls import router
from book.views import BookViewSet


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



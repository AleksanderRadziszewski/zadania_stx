from django.test import TestCase, Client
from django.urls import reverse, resolve
from book.models import Book


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse("book import")
        self.welcome = reverse("welcome")
        self.book_list = reverse("search book list")
        self.update_url = reverse("update", kwargs={"pk": 1})
        Book.objects.create(
            title="TestCase",
            author="TestCase",
            pub_date="2020",
            isbn_num="9781426749490",
            pages_amount=666,
            pub_language="EN",
            link="http://www.google.pl",
        )

    def test_book_list_import_GET(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "book/search_import.html")

    def test_book_add_update_GET(self):
        response = self.client.get(self.update_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "book/edit_book.html")

    def test_search_book_list_GET(self):
        response = self.client.get(self.book_list)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "book/form.html")

    def test_welcome_GET(self):
        response = self.client.get("")

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "book/welcome.html")


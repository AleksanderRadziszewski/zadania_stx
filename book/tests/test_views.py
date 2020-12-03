from django.test import TestCase, Client
from django.urls import reverse
from book.models import Book


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse("book import")
        self.welcome = reverse("welcome")
        self.book_list = reverse("search book list")
        self.url_add = reverse("add")
        self.book = Book.objects.create(
            title="FirstBook",
            author="TestCase",
            pub_date="2020",
            isbn_num="9781426749490",
            pages_amount=666,
            pub_language="EN",
            link="http://www.google.pl",
        )

        self.update_url = reverse("update", kwargs={"pk": self.book.id})

    def test_book_list_import_GET(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "book/search_import.html")

    def test_book_update_GET(self):
        response = self.client.get(self.update_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "book/edit_book.html")

    def test_book_add_GET(self):
        response = self.client.get(self.url_add)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "book/edit_book.html")

    def test_book_list_GET(self):
        response = self.client.get(self.book_list)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "book/form.html")

    def test_welcome_GET(self):
        response = self.client.get("")

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "book/welcome.html")

    def test_book_add_POST(self):
        response = self.client.post(
            self.add_url,
            {
                "title": "Harry",
                "author": "me",
                "pub_date": "2020",
                "isbn_num": "9781426749490",
                "pages_amount": 666,
                "pub_language": "EN",
                "link": "http://www.google.pl",
            }, follow=True
        )
        test_case = Book.objects.all().last()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(test_case.title, "Harry")

    def test_book_update_POST(self):
        response = self.client.post(
            self.update_url,
            {

                "title": "Edit by me",
                "author": "Edit",
                "pub_date": "2020",
                "isbn_num": "9781426749490",
                "pages_amount": 666,
                "pub_language": "EN",
                "link": "http://www.google.pl",
            },
        )

        self.book.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.book.title, "Edit by me")


    def test_book_create_no_data(self):
        response = self.client.post(self.url_add, {})
        books = Book.objects.all().count()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(books, 1)

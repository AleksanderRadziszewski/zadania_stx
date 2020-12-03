from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from book.models import Book
from book.serializers import BookSerializer


class BookTest(APITestCase):

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

    def test_book_create(self):
        data_create = {
            "pk": 1,
            "title": "Rest Api Test create",
            "author": "me",
            "pub_date": "2009",
            "isbn_num": "9781426749490",
            "pages_amount": 777,
            "pub_language": "EN",
            "link": "http://www.google.pl",
        }

        response = self.client.post(self.url_add, data_create, format="json")
        test_case_create = Book.objects.all().last()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(test_case_create.title, "Rest Api Test create")

    def test_book_update(self):
        data_update = BookSerializer(self.data_set_up).data
        data_update["title"] = "Rest Api Test update"

        response = self.client.put(self.url_edit, data_update, format="json")
        test_case_update = Book.objects.get()
        self.data_set_up.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(test_case_update.title, "Rest Api Test update")

    def test_book_delete(self):
        data_delete = BookSerializer(self.data_set_up).data
        data_delete["title"] = "Rest Api delete"

        response = self.client.delete(self.url_edit, data_delete, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)



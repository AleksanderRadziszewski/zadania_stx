from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from book.models import Book


class BookTest(APITestCase):

    def setUp(self):
        self.url = reverse("book-list")
        self.data_set_up = {
            "title": "Rest Api Test",
            "author": "me",
            "pub_date": "2020",
            "isbn_num": "9781426749490",
            "pages_amount": 666,
            "pub_language": "EN",
            "link": "http://www.google.pl",
        }
        self.object = self.client.post(self.url, self.data_set_up, format='json')

    def test_create_book(self):
        data_create = {
            "title": "Rest Api Test create",
            "author": "me",
            "pub_date": "2009",
            "isbn_num": "9781426749490",
            "pages_amount": 777,
            "pub_language": "EN",
            "link": "http://www.google.pl",
        }

        response = self.client.post(self.url, data_create, format="json")
        test_case_create = Book.objects.all().last()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(test_case_create.title, "Rest Api Test create")

    def test_update_book(self):
        data_update = self.data_set_up
        data_update["title"] = "Rest Api Test update"

        response=self.client.post(self.url, data_update, format="json")
        test_case_update= Book.objects.all().last()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(test_case_update.title, "Rest Api Test update")

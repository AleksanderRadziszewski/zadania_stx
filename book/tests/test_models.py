from django.test import TestCase

from book.models import Book


class TestBookModel(TestCase):

    def setUp(self):
        self.book = Book.objects.create(
            title="First Book",
            author="TestCase",
            pub_date="2020",
            isbn_num="9781426749490",
            pages_amount=666,
            pub_language="EN",
            link="http://www.google.pl",
        )

    def test_book_is_assigned_slug_on_creation(self):
        self.assertEquals(self.book.slug, 'first-book')
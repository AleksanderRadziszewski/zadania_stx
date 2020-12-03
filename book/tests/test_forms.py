from django.test import SimpleTestCase
from book.forms import SearchForm


class TestForms(SimpleTestCase):

    def test_book_form_valid_data(self):
        form = SearchForm(data={
            "search_input": "Harry Potter",
            "pub_date_since": "2009",
            "pub_date_to": "2020"
        })

        self.assertTrue(form.is_valid())

    def test_book_form_no_data(self):
        form = SearchForm(data={})

        self.assertFalse(form.is_valid())
        self.assertRaises(KeyError, form.clean())
        self.assertEquals(len(form.errors), 3)


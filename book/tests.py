from django.test import Client, TestCase
from django.urls import reverse


class TestSearchViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.search = reverse("search")

    def test_search_GET_true(self):
        response = self.client.get(self.search)
        self.assertTemplateUsed(response, "book/books_table.html")

    def test_search_GET_false(self):
        response = self.client.get(self.search)
        self.assertTemplateNotUsed(response, "book/books_table.html")


class TestUpdateView(TestCase):
    def setUp(self):
        self.client = Client()
        self.add_update = reverse("update", kwargs={"pk": 358})

    def test_update_add_GET_true(self):
        response = self.client.get(self.add_update)
        self.assertTemplateUsed(response, "book/edit_book.html")

    def test_update_add_GET_false(self):
        response = self.client.get(self.add_update)
        self.assertTemplateNotUsed(response, "book/edit_book.html")

    def test_update_add_POST_true(self):
        response = self.client.get(self.add_update)
        self.assertEqual(response, 200)
        self.assertEqual(response.status_code, 200)

    def test_update_add_POST_false(self):
        response = self.client.get(self.add_update)
        self.assertNotEqual(response, 200)
        self.assertNotEqual(response.status_code, 200)


class TestSearchApi(TestCase):
    def setUp(self):
        self.client = Client()
        self.search_api = reverse("search api")

    def test_search_api_GET_true(self):
        response = self.client.get(self.search_api)
        self.assertTemplateUsed(response, "book/search.html")

    def test_search_api_GET_false(self):
        response = self.client.get(self.search_api)
        self.assertTemplateNotUsed(response, "book/search.html")

    def test_search_api_POST_true(self):
        response = self.client.get(self.search_api)
        self.assertEqual(response, 200)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "book/search_api.html")

    def test_search_api_POST_false(self):
        response = self.client.get(self.search_api)
        self.assertNotEqual(response, 200)
        self.assertNotEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response, "book/search_api.html")


class TestFilterApi(TestCase):
    def setUp(self):
        self.client = Client()
        self.filter_api = reverse("filter")

    def test_filter_api_GET_true(self):
        response = self.client.get(self.filter_api)
        self.assertTemplateUsed(response, "book/filter.html")

    def test_filter_api_GET_false(self):
        response = self.client.get(self.filter_api)
        self.assertTemplateNotUsed(response, "book/filter.html")

    def test_filter_api_POST_true(self):
        response = self.client.get(self.filter_api)
        self.assertEqual(response, 200)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "book/book_search_api.html")

    def test_filter_api_POST_false(self):
        response = self.client.get(self.filter_api)
        self.assertNotEqual(response, 200)
        self.assertNotEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response, "book/book_search_api.html")


class TestBookImport(TestCase):
    def setUp(self):
        self.client = Client()
        self.book_import = reverse("book import")

    def test_book_import_GET_true(self):
        response = self.client.get(self.book_import)
        self.assertTemplateUsed(response, "book/search.html")

    def test_book_import_GET_false(self):
        response = self.client.get(self.book_import)
        self.assertTemplateNotUsed(response, "book/search.html")

    def test__book_import_POST_true(self):
        response = self.client.get(self.book_import)
        self.assertEqual(response, 200)
        self.assertEqual(response.status_code, 200)

    def test_book_import_POST_false(self):
        response = self.client.get(self.book_import)
        self.assertNotEqual(response, 200)
        self.assertNotEqual(response.status_code, 200)

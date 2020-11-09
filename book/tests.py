from django.test import Client, TestCase
from django.urls import reverse


class TestWelcomeView(TestCase):
    def setUp(self):
        self.client = Client()
        self.search = reverse("welcome")

    def test_welcome_GET_true(self):
        response = self.client.get(self.search)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "book/welcome.html")

    def test_welcome_GET_false(self):
        response = self.client.get(self.search)
        self.assertNotEqual(response.status_code, 500)
        self.assertTemplateNotUsed(response, "book/edit_book.html")


class TestSearchViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.search = reverse("search")

    def test_search_GET_true(self):
        response = self.client.get(self.search)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "book/form.html")

    def test_search_GET_false(self):
        response = self.client.get(self.search)
        self.assertNotEqual(response.status_code, 500)
        self.assertTemplateNotUsed(response, "book/edit_book.html")

    def test_search_POST_true(self):
        response = self.client.post(self.search)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "book/books_table.html")

    def test_search_POST_false(self):
        response = self.client.post(self.search)
        self.assertNotEqual(response.status_code, 500)
        self.assertTemplateNotUsed(response, "book/filter.html")


class TestUpdateView(TestCase):
    def setUp(self):
        self.client = Client()
        self.add_update = reverse("update", kwargs={"pk": 428})

    def test_update_add_GET_true(self):
        response = self.client.get(self.add_update)
        self.assertTemplateUsed(response, "book/edit_book.html")

    def test_update_add_GET_false(self):
        response = self.client.get(self.add_update)
        self.assertTemplateNotUsed(response, "book/filter.html")

    def test_update_add_POST_true(self):
        response = self.client.post(self.add_update,follow=True)
        self.assertEqual(response.status_code, 200)

    def test_update_add_POST_false(self):
        response = self.client.post(self.add_update)
        self.assertNotEqual(response, 500)
        self.assertNotEqual(response.status_code, 500)


class TestSearchApi(TestCase):
    def setUp(self):
        self.client = Client()
        self.search_api = reverse("search api")

    def test_search_api_GET_true(self):
        response = self.client.get(self.search_api)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "book/book_search_api.html")

    def test_search_api_GET_false(self):
        response = self.client.get(self.search_api)
        self.assertNotEqual(response.status_code, 500)
        self.assertTemplateNotUsed(response, "book/filter.html")

    def test_search_api_POST_true(self):
        response = self.client.post(self.search_api)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "book/book_list_api.html")

    def test_search_api_POST_false(self):
        response = self.client.post(self.search_api)
        self.assertNotEqual(response.status_code, 500)
        self.assertTemplateNotUsed(response, "book/filter.html")


class TestFilterApi(TestCase):
    def setUp(self):
        self.client = Client()
        self.filter_api = reverse("filter api")

    def test_filter_api_GET_true(self):
        response = self.client.get(self.filter_api)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "book/filter.html")

    def test_filter_api_GET_false(self):
        response = self.client.get(self.filter_api)
        self.assertTemplateNotUsed(response, "book/book_list_api.html")

    def test_filter_api_POST_true(self):
        response = self.client.post(self.filter_api)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "book/filter_book_api.html")

    def test_filter_api_POST_false(self):
        response = self.client.post(self.filter_api)
        self.assertNotEqual(response.status_code, 500)
        self.assertTemplateNotUsed(response, "book/book_list_api.html")


class TestBookImport(TestCase):
    def setUp(self):
        self.client = Client()
        self.book_import = reverse("book import")

    def test_book_import_GET_true(self):
        response = self.client.get(self.book_import)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "book/search_import.html")

    def test_book_import_GET_false(self):
        response = self.client.get(self.book_import)
        self.assertNotEqual(response.status_code, 500)
        self.assertTemplateNotUsed(response, "book/book_list_api.html")

    def test__book_import_POST_true(self):
        response = self.client.post(self.book_import)
        self.assertEqual(response.status_code, 200)

    def test_book_import_POST_false(self):
        response = self.client.post(self.book_import)
        self.assertNotEqual(response.status_code, 500)
        self.assertTemplateNotUsed(response, "book/book_list_api.html")

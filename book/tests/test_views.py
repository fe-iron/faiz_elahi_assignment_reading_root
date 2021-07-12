from django.test import Client, TestCase
from django.urls import reverse
from book.models import Book


class TestViews(TestCase):
    """
        This is the Test case for the urls, so now we'll be checking for the index url
    """
    def setUp(self):
        self.client = Client()
        self.index_url = reverse("index")
        self.viewbook_url = reverse("view-book")
        self.storebook_url = reverse("store-book")
        self.detailedview_url = reverse("detailed-view", args=['1'])
        self.book = Book.objects.create(
            name="test book",
            author="test author",
            genre="test genre",
            language="test language"
        )

    def test_index_view_resolved(self):
        response = self.client.get(self.index_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_viewbook_view_resolved(self):
        response = self.client.get(self.viewbook_url)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.book.name, "test book")
        self.assertTemplateUsed(response, "view-book.html")

    def test_detailed_view_resolved(self):
        response = self.client.get(self.detailedview_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "detailed-view.html")

    def test_store_books_resolved(self):
        response = self.client.get(self.storebook_url)

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, "/view-book")

    def test_store_books_with_data(self):
        response = self.client.post(self.storebook_url, {
            'name': "test book",
            'author': "test author",
            'genre': "test genre",
            'language': "test language"
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.book.name, 'test book')

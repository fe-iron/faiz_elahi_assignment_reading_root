from django.test import Client, TestCase
from django.urls import reverse
from book.models import Book

class TestBookModel(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            name = "book test",
            author = "book author",
            language = "book language",
            genre = "test genre"
        )

    def test_book_model(self):
        self.assertEquals(self.book.name, "book test")
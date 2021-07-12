from django.test import SimpleTestCase
from django.urls import reverse, resolve
from book.views import Index, ViewBook, DetailedView


class TestUrls(SimpleTestCase):
    """
        This is the Test case for the urls, so now we'll be checking for the index url
    """
    def setUp(self):
        self.index_urls = reverse("index")
        self.view_book_urls = reverse("view-book")
        self.detailed_book_urls = reverse("detailed-view", args=['1'])

    def test_index_urls(self):
        self.assertEquals(resolve(self.index_urls).func.view_class, Index)

    def test_viewboook_urls(self):
        self.assertEquals(resolve(self.view_book_urls).func.view_class, ViewBook)

    def test_detailed_urls(self):
        self.assertEquals(resolve(self.detailed_book_urls).func.view_class, DetailedView)
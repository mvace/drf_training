from .base import BaseAPITestCase


class BookViewsetViewTestCase(BaseAPITestCase):

    def listURL(self):
        print("Running: book-list")
        return "book-list"

    def detailURL(self):
        print("Running: book-detail")
        return "book-detail"

    def test_create_book(self):
        self._create_book()

    def test_get_book(self):
        self._get_book()

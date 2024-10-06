from .base import BaseAPITestCase


class BookFBVAPITestCase(BaseAPITestCase):

    def listURL(self):
        print("Running: book-list-fbv")
        return "book-list-fbv"

    def detailURL(self):
        print("Running: book-detail-fbv")
        return "book-detail-fbv"

    def test_create_book(self):
        self._create_book()

    def test_get_book(self):
        self._get_book()

from .base import BaseAPITestCase


class BookCBVGenericTestCase(BaseAPITestCase):

    def listURL(self):
        print("Running: book-list-generic-cbv")
        return "book-list-generic-cbv"

    def detailURL(self):
        print("Running: book-detail-generic-cbv")
        return "book-detail-generic-cbv"

    def test_create_book(self):
        self._create_book()

    def test_get_book(self):
        self._get_book()

from .base import BaseAPITestCase


class CBVAPIViewTestCase(BaseAPITestCase):

    def listURL(self):
        print("Running: book-list-cbv-apiviews")
        return "book-list-cbv-apiviews"

    def detailURL(self):
        print("Running: book-detail-cbv-apiviews")
        return "book-detail-cbv-apiviews"

    def test_create_book(self):
        self._create_book()

    def test_get_book(self):
        self._get_book()

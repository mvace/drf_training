from .base import BaseAPITestCase


class BookCBVconcreteGenericViewTestCase(BaseAPITestCase):

    def listURL(self):
        print("Running: book-list-concrete-generic-cbv")
        return "book-list-concrete-generic-cbv"

    def detailURL(self):
        print("Running: book-detail-concrete-generic-cbv")
        return "book-detail-concrete-generic-cbv"

    def test_create_book(self):
        self._create_book()

    def test_get_book(self):
        self._get_book()

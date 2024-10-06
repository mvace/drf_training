from .base import BaseAPITestCase


class BookMixinViewTestCase(BaseAPITestCase):

    def listURL(self):
        print("Running: book-list-mixin-cbv")
        return "book-list-mixin-cbv"

    def detailURL(self):
        print("Running: book-detail-mixin-cbv")
        return "book-detail-mixin-cbv"

    def test_create_book(self):
        self._create_book()

    def test_get_book(self):
        self._get_book()

from .base import BaseAPITestCase


class BookMixinViewTestCase(BaseAPITestCase):

    def listURL(self):
        print("Running: book-list-mixin-cbv")
        return "book-list-mixin-cbv"

    def detailURL(self):
        print("Running: book-detail-mixin-cbv")
        return "book-detail-mixin-cbv"

    def test_list_books(self):
        self._list_books()

    def test_create_book(self):
        self._create_book()

    def test_retrieve_book(self):
        self._retrieve_book()

    def test_update_book(self):
        self._update_book()

    def test_delete_book(self):
        self._delete_book()

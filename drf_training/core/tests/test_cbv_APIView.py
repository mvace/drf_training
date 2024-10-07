from .base import BaseAPITestCase


class CBVAPIViewTestCase(BaseAPITestCase):

    def listURL(self):
        print("Running: book-list-cbv-apiviews")
        return "book-list-cbv-apiviews"

    def detailURL(self):
        print("Running: book-detail-cbv-apiviews")
        return "book-detail-cbv-apiviews"

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

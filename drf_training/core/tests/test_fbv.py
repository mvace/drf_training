from .base import BaseAPITestCase


class BookFBVAPITestCase(BaseAPITestCase):

    def listURL(self):
        print("Running: book-list-fbv")
        return "book-list-fbv"

    def detailURL(self):
        print("Running: book-detail-fbv")
        return "book-detail-fbv"

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

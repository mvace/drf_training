from .base import BaseAPITestCase


class BookCBVconcreteGenericViewTestCase(BaseAPITestCase):

    def listURL(self):
        print("Running: book-list-concrete-generic-cbv")
        return "book-list-concrete-generic-cbv"

    def detailURL(self):
        print("Running: book-detail-concrete-generic-cbv")
        return "book-detail-concrete-generic-cbv"

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

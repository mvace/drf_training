from .base import BaseAPITestCaseBook, BaseAPITestCaseAuthor


class BookCBVGenericTestCase(BaseAPITestCaseBook):

    def listURL(self):
        return "book-list-generic-cbv"

    def detailURL(self):
        return "book-detail-generic-cbv"

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


class AuthorCBVGenericTestCase(BaseAPITestCaseAuthor):

    def listURL(self):
        return "author-list-generic-cbv"

    def detailURL(self):
        return "author-detail-generic-cbv"

    def test_list_authors(self):
        self._list_authors()

    def test_create_author(self):
        self._create_author()

    def test_retrieve_author(self):
        self._retrieve_author()

    def test_update_author(self):
        self._update_author()

    def test_delete_author(self):
        self._delete_author()

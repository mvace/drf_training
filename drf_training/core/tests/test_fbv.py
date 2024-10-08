from .base import BaseAPITestCaseBook, BaseAPITestCaseAuthor


class BookFBVAPITestCase(BaseAPITestCaseBook):

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


class AuthorFBVAPITestCase(BaseAPITestCaseAuthor):

    def listURL(self):
        print("Running: author-list-fbv")
        return "author-list-fbv"

    def detailURL(self):
        print("Running: author-detail-fbv")
        return "author-detail-fbv"

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

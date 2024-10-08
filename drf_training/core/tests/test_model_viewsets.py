from .base import BaseAPITestCaseBook, BaseAPITestCaseAuthor


class BookModelViewsetViewTestCase(BaseAPITestCaseBook):

    def listURL(self):
        print("Running: modelbook-list")
        return "modelbook-list"

    def detailURL(self):
        print("Running: modelbook-detail")
        return "modelbook-detail"

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


class AuthorModelViewsetViewTestCase(BaseAPITestCaseAuthor):

    def listURL(self):
        print("Running: modelauthor-list")
        return "modelauthor-list"

    def detailURL(self):
        print("Running: modelauthor-detail")
        return "modelauthor-detail"

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

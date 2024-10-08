from .base import BaseAPITestCaseBook, BaseAPITestCaseAuthor


class CBVAPIViewBookTestCase(BaseAPITestCaseBook):

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


class CBVAPIViewAuthorTestCase(BaseAPITestCaseAuthor):

    def listURL(self):
        print("Running: author-list-cbv-apiviews")
        return "author-list-cbv-apiviews"

    def detailURL(self):
        print("Running: author-detail-cbv-apiviews")
        return "author-detail-cbv-apiviews"

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

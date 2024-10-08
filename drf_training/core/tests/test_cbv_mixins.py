from .base import BaseAPITestCaseBook, BaseAPITestCaseAuthor


class BookMixinViewTestCase(BaseAPITestCaseBook):

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


class AuthorMixinViewTestCase(BaseAPITestCaseAuthor):

    def listURL(self):
        print("Running: author-list-mixin-cbv")
        return "author-list-mixin-cbv"

    def detailURL(self):
        print("Running: author-detail-mixin-cbv")
        return "author-detail-mixin-cbv"

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

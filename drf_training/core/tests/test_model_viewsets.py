from .base import BaseAPITestCase


class BookModelViewsetViewTestCase(BaseAPITestCase):

    def listURL(self):
        print("Running: modelbook-list")
        return "modelbook-list"

    def detailURL(self):
        print("Running: modelbook-detail")
        return "modelbook-detail"

    def test_create_book(self):
        self._create_book()

    def test_get_book(self):
        self._get_book()

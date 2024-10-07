from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from ..models import Book, Author, User
from ..serializers import BookSerializer, AuthorSerializer
from datetime import datetime


class BaseAPITestCase(TestCase):

    def listURL(self):
        return "book-list-fbv"

    def detailURL(self):
        return "book-detail-fbv"

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        birth_date = datetime(1980, 9, 1)
        self.author = Author.objects.create(name="Test Author", birth_date=birth_date)
        self.book = Book.objects.create(
            title="Test Book",
            published_date=datetime(2020, 1, 1),
            author=self.author,
            owner=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def _list_books(self):
        url = reverse(self.listURL())
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Test Book")

    def _create_book(self):
        url = reverse(self.listURL())
        data = {
            "title": "New Book",
            "published_date": "2021-01-01",
            "author": self.author.id,
            "owner": self.user.id,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(response.data["title"], "New Book")

    def _retrieve_book(self):
        url = reverse(self.detailURL(), kwargs={"pk": self.book.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Book")

    def _update_book(self):
        url = reverse(self.detailURL(), kwargs={"pk": self.book.id})
        data = {
            "title": "Updated Book Title",
            "published_date": "2022-01-01",
            "author": self.author.id,
            "owner": self.user.id,
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book Title")

    def _delete_book(self):
        url = reverse(self.detailURL(), kwargs={"pk": self.book.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

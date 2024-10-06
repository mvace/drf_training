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
        self.published_date = datetime(2018, 9, 1)
        self.birth_date = datetime(1980, 9, 1)
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )
        self.client.force_authenticate(user=self.user)
        self.author = Author.objects.create(
            name="John Author", birth_date=self.birth_date
        )
        self.book_data = {
            "title": "Test Book",
            "published_date": self.published_date.date().isoformat(),
            "author": self.author.id,
        }

    def _create_book(self):
        url = reverse(self.listURL())
        response = self.client.post(url, self.book_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, "Test Book")
        created_book = Book.objects.get()
        self.assertEqual(created_book.owner, self.user)

    def _get_book(self):
        self.book = Book.objects.create(
            title="Test Book",
            published_date=self.published_date,
            author=self.author,
            owner=self.user,
        )
        url = reverse(self.detailURL(), kwargs={"pk": self.book.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

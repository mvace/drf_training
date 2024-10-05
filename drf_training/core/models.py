from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Author(models.Model):
    name = models.CharField(max_length=128)
    birth_date = models.DateField(default=datetime(1970, 1, 1))
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="author", default=1
    )

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=128)
    published_date = models.DateField(default=datetime(1990, 1, 1))
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return self.title

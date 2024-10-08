from rest_framework.viewsets import ModelViewSet
from ..serializers import (
    BookSerializer,
    AuthorSerializer,
    ModelBookSerializer,
    ModelAuthorSerializer,
)
from ..models import Book, Author
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from ..permissions import IsOwnerOrStaffOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = ModelBookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrStaffOrReadOnly]


class AuthorModelViewset(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = ModelAuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrStaffOrReadOnly]

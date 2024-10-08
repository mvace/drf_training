from rest_framework import generics, permissions
from ..serializers import (
    BookSerializer,
    AuthorSerializer,
    ModelBookSerializer,
    ModelAuthorSerializer,
)
from ..models import Book, Author
from ..permissions import IsOwnerOrStaffOrReadOnly


class GenericsBookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = ModelBookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GenericsBookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = ModelBookSerializer
    permission_classes = [IsOwnerOrStaffOrReadOnly]


class GenericsAuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = ModelAuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GenericsAuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = ModelAuthorSerializer
    permission_classes = [IsOwnerOrStaffOrReadOnly]

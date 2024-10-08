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


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = ModelBookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrStaffOrReadOnly]


class AuthorModelViewset(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = ModelAuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrStaffOrReadOnly]

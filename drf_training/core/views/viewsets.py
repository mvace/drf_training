from rest_framework.viewsets import ViewSet
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from ..serializers import (
    BookSerializer,
    AuthorSerializer,
    ModelBookSerializer,
    ModelAuthorSerializer,
)
from ..models import Book, Author
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from ..permissions import IsOwnerOrStaffOrReadOnly


class BookViewSet(ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrStaffOrReadOnly]

    def get_object(self, pk):
        return get_object_or_404(Book, pk=pk)

    def list(self, request):
        queryset = Book.objects.all()
        serializer = ModelBookSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ModelBookSerializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        book = self.get_object(pk=pk)
        serializer = ModelBookSerializer(book)
        return Response(serializer.data)

    def update(self, request, pk=None):
        book = self.get_object(pk=pk)
        serializer = ModelBookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        book = self.get_object(pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AuthorViewSet(ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrStaffOrReadOnly]

    def get_object(self, pk):
        return get_object_or_404(Author, pk=pk)

    def list(self, request):
        queryset = Author.objects.all()
        serializer = ModelAuthorSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ModelAuthorSerializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        author = self.get_object(pk=pk)
        serializer = ModelAuthorSerializer(author)
        return Response(serializer.data)

    def update(self, request, pk=None):
        author = self.get_object(pk=pk)
        serializer = ModelAuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        author = self.get_object(pk=pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

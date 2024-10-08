from rest_framework.views import APIView
from ..models import User, Book, Author
from ..serializers import (
    BookSerializer,
    AuthorSerializer,
    ModelBookSerializer,
    ModelAuthorSerializer,
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from ..permissions import IsOwnerOrStaffOrReadOnly
from django.shortcuts import get_object_or_404


class BookListCBV(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = ModelBookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ModelBookSerializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetailCBV(APIView):
    permission_classes = [IsOwnerOrStaffOrReadOnly]

    def get_object(self, pk):
        return get_object_or_404(Book, id=pk)

    def get(self, request, pk, format=None):
        book = self.get_object(pk=pk)
        serializer = ModelBookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        book = self.get_object(pk=pk)
        serializer = ModelBookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        book = self.get_object(pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AuthorListCBV(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        authors = Author.objects.all()
        serializer = ModelAuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ModelAuthorSerializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorDetailCBV(APIView):
    permission_classes = [IsOwnerOrStaffOrReadOnly]

    def get_object(self, pk):
        return get_object_or_404(Author, pk=pk)

    def get(self, request, pk, format=None):
        author = self.get_object(pk=pk)
        serializer = ModelAuthorSerializer(author)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        author = self.get_object(pk=pk)
        serializer = ModelAuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        author = self.get_object(pk=pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

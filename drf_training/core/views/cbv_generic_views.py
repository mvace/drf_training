from rest_framework import generics, permissions, status
from ..serializers import BookSerializer, AuthorSerializer, ModelBookSerializer
from ..models import Book, Author
from ..permissions import IsOwnerOrStaffOrReadOnly
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class GenericsBookList(generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = ModelBookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        books = self.get_queryset()
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.get_serializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenericsBookDetail(generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = ModelBookSerializer
    permission_classes = [IsOwnerOrStaffOrReadOnly]

    def get_object(self, pk):
        return get_object_or_404(Book, pk=pk)

    def get(self, request, pk):
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


class GenericAuthorList(generics.GenericAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        authors = self.get_queryset()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.get_serializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenericAuthorDetail(generics.GenericAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsOwnerOrStaffOrReadOnly]

    def get_object(self, pk):
        return get_object_or_404(Author, pk=pk)

    def get(self, request, pk):
        author = self.get_object(pk=pk)
        print(f"author: {author}")
        serializer = AuthorSerializer(author)
        print(f"serializer: {serializer}")
        return Response(serializer.data)

    def put(self, request, pk):
        author = self.get_object(pk=pk)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        author = self.get_object(pk=pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

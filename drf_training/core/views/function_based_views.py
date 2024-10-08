from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from ..models import User, Book, Author
from ..serializers import (
    BookSerializer,
    AuthorSerializer,
    ModelBookSerializer,
    ModelAuthorSerializer,
)
from rest_framework import status
from ..permissions import IsOwnerOrStaffOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticatedOrReadOnly])
def book_list_function_based_view(request):
    if request.method == "GET":
        books = Book.objects.all()
        serializer = ModelBookSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ModelBookSerializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsOwnerOrStaffOrReadOnly])
def book_detail_function_based_view(request, pk):
    book = get_object_or_404(Book, id=pk)

    if request.method == "GET":
        serializer = ModelBookSerializer(book)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ModelBookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticatedOrReadOnly])
def author_list_function_based_view(request):
    if request.method == "GET":
        authors = Author.objects.all()
        serializer = ModelAuthorSerializer(authors, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = ModelAuthorSerializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsOwnerOrStaffOrReadOnly])
def author_detail_function_based_view(request, pk):
    author = get_object_or_404(Author, pk=pk)

    if request.method == "GET":
        serializer = ModelAuthorSerializer(author)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = ModelAuthorSerializer(author, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

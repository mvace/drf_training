from django.shortcuts import render, get_object_or_404
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from ..models import User, Book, Author
from ..serializers import BookSerializer
from rest_framework import status
from ..permissions import IsOwnerOrStaffOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticatedOrReadOnly])
def book_list_function_based_view(request):
    if request.method == "GET":
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = BookSerializer(data=request.data, context={"request": request})
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsOwnerOrStaffOrReadOnly])
def book_detail_function_based_view(request, pk):
    book = get_object_or_404(Book, id=pk)

    if request.method == "GET":
        serializer = BookSerializer(book)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "books-fbv": reverse("book-list-fbv", request=request, format=format),
            "books-cbv-apivew": reverse(
                "book-list-cbv-apiviews", request=request, format=format
            ),
        }
    )

from rest_framework.views import APIView
from ..models import User, Book, Author
from ..serializers import BookSerializer
from rest_framework.response import Response


class BookListCBV(APIView):
    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)  
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data) # context={"request": request}


class BookDetailCBV(APIView):
    def get(self, request, pk, format=None):
        book = Book.objects.get(id=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

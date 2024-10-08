from rest_framework.viewsets import ModelViewSet
from ..serializers import ModelBookSerializer, ModelAuthorSerializer
from ..models import Author, Book
from ..permissions import IsOwnerOrStaffOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class BookModelViewSetAction(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = ModelBookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrStaffOrReadOnly]

    @action(detail=False)
    def recently_published(self, request):
        last_five = Book.objects.all().order_by("-published_date")[:5]
        serializer = self.get_serializer(last_five, many=True)
        if last_five:
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorModelViewSetAction(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = ModelAuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrStaffOrReadOnly]

    @action(detail=False)
    def youngest(self, request):
        last_five = Author.objects.all().order_by("-birth_date")[:5]
        serializer = self.get_serializer(last_five, many=True)
        if last_five:
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

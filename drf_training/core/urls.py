from django.urls import path, include
from .views import (
    function_based_views,
    cbv_APIView,
    cbv_generic_views,
    cbv_concrete_generic_views,
    cbv_mixins,
    viewsets,
    model_viewsets,
)
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router2 = SimpleRouter()
router.register(r"books", viewsets.BookViewSet, basename="book")
router.register(r"author", viewsets.AuthorViewSet, basename="author")
router2.register(r"books", model_viewsets.BookModelViewSet, basename="modelbook")
router2.register(r"author", model_viewsets.AuthorModelViewset, basename="modelauthor")


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "books-fbv": reverse("book-list-fbv", request=request, format=format),
            "books-cbv-apivew": reverse(
                "book-list-cbv-apiviews", request=request, format=format
            ),
            "books-generic-cbv": reverse(
                "book-list-generic-cbv", request=request, format=format
            ),
            "books-concrete-generic-cbv": reverse(
                "book-list-concrete-generic-cbv", request=request, format=format
            ),
            "authors-concrete-generic-cbv": reverse(
                "author-list-concrete-generic-cbv", request=request, format=format
            ),
            "books-mixin-cbv": reverse(
                "book-list-mixin-cbv", request=request, format=format
            ),
            "books-viewset": reverse("book-list", request=request, format=format),
            "authors-viewset": reverse("author-list", request=request, format=format),
            "books-model-viewset": reverse(
                "modelbook-list", request=request, format=format
            ),
            "author-model-viewset": reverse(
                "modelauthor-list", request=request, format=format
            ),
        }
    )


urlpatterns = [
    # API Root:
    path("", api_root),
    # Function Based Views:
    path(
        "fbv/books/",
        function_based_views.book_list_function_based_view,
        name="book-list-fbv",
    ),
    path(
        "fbv/books/<int:pk>",
        function_based_views.book_detail_function_based_view,
        name="book-detail-fbv",
    ),
    # Class Based Views using APIView:
    path(
        "cbv-apiview/books/",
        cbv_APIView.BookListCBV.as_view(),
        name="book-list-cbv-apiviews",
    ),
    path(
        "cbv-apiview/books/<int:pk>",
        cbv_APIView.BookDetailCBV.as_view(),
        name="book-detail-cbv-apiviews",
    ),
    # Generic class-based views
    path(
        "generic-cbv/books/",
        cbv_generic_views.GenericsBookList.as_view(),
        name="book-list-generic-cbv",
    ),
    path(
        "generic-cbv/books/<int:pk>",
        cbv_generic_views.GenericsBookDetail.as_view(),
        name="book-detail-generic-cbv",
    ),
    # Mixins with generic class-based views
    path(
        "mixin-cbv/books/",
        cbv_mixins.MixinBookList.as_view(),
        name="book-list-mixin-cbv",
    ),
    path(
        "mixin-cbv/books/<int:pk>",
        cbv_mixins.MixinBookDetail.as_view(),
        name="book-detail-mixin-cbv",
    ),
    # Concrete generic class-based views
    path(
        "concrete-generic-cbv/books/",
        cbv_concrete_generic_views.GenericsBookList.as_view(),
        name="book-list-concrete-generic-cbv",
    ),
    path(
        "concrete-generic-cbv/books/<int:pk>",
        cbv_concrete_generic_views.GenericsBookDetail.as_view(),
        name="book-detail-concrete-generic-cbv",
    ),
    path(
        "concrete-generic-cbv/authors/",
        cbv_concrete_generic_views.GenericsAuthorList.as_view(),
        name="author-list-concrete-generic-cbv",
    ),
    path(
        "concrete-generic-cbv/authors/<int:pk>",
        cbv_concrete_generic_views.GenericsAuthorDetail.as_view(),
        name="author-detail-concrete-generic-cbv",
    ),
    # ViewSets
    path("viewset/", include(router.urls)),
    # ModelViewSets
    path("model_viewset/", include(router2.urls)),
    # Custom ViewSets with custom actions
]

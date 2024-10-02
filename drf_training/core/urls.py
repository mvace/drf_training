from django.urls import path
from .views import function_based_views, cbv_APIView


urlpatterns = [
    # API Root:
    path("", function_based_views.api_root),
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
    # Mixins with generic class-based views
    # Concrete generic class-based views
    # ViewSets
    # ModelViewSets
    # Custom ViewSets with custom actions
]

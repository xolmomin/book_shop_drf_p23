from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, RetrieveAPIView

from shared.paginations import CustomPageNumberPagination
from shops.models import Book
from shops.serializers import BookListModelSerializer, BookDetailModelSerializer


@extend_schema(tags=['shops'])
class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListModelSerializer
    pagination_class = CustomPageNumberPagination


@extend_schema(tags=['shops'])
class BookRetrieveAPIView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailModelSerializer
    lookup_field = 'slug'

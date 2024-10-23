from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView

from shared.paginations import CustomPageNumberPagination
from shops.models import Book
from shops.serializers import BookListModelSerializer


@extend_schema(tags=['shops'])
class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListModelSerializer
    pagination_class = CustomPageNumberPagination

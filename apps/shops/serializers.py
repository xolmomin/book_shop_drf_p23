from rest_framework.serializers import ModelSerializer

from shops.models import Book
from users.serializers import AuthorListModelSerializer, AuthorDetailModelSerializer


class BookDetailModelSerializer(ModelSerializer):
    author = AuthorDetailModelSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        exclude = ()


class BookListModelSerializer(ModelSerializer):
    author = AuthorListModelSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = 'id', 'title', 'slug', 'author', 'image'

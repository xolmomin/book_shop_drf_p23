from rest_framework.serializers import ModelSerializer

from shops.models import Book
from users.serializers import AuthorModelSerializer


class BookDetailModelSerializer(ModelSerializer):
    class Meta:
        model = Book
        exclude = ()


class BookListModelSerializer(ModelSerializer):
    author = AuthorModelSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ('title', 'slug', 'author', 'image')

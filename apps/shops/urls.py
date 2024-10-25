from django.urls import path

from shops.views import BookListAPIView, BookRetrieveAPIView

urlpatterns = [
    path('books', BookListAPIView.as_view(), name='book-list'),
    path('books/<str:slug>', BookRetrieveAPIView.as_view(), name='book-detail'),
]

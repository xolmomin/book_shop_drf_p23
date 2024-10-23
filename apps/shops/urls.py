from django.urls import path

from shops.views import BookListAPIView

urlpatterns = [
    path('books', BookListAPIView.as_view(), name='book-list'),
    path('books/<str:slug>', BookListAPIView.as_view(), name='book-list'),
]

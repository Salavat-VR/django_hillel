from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from api.generics import PostSerializer, BookSerializer
from main.models import Post, Book


class PostApiViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("id")
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination


class BookApiViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by("id")
    serializer_class = BookSerializer
    pagination_class = PageNumberPagination

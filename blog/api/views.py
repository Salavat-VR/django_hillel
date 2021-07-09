from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from api.generics import PostSerializer
from main.models import Post


class PostApiViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("id")
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination

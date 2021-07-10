from rest_framework import serializers

from main.models import Post, Book


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id",
                  "title",
                  "description",
                  "content",
                  "created",
                  "updated")


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("id",
                  "title",
                  "author",
                  "category")

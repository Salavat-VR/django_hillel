from django.core.cache import cache

from .models import Post


def post_all():
    my_key = Post.cache_key()
    if my_key in cache:
        posts = cache.get(my_key)
    else:
        posts = Post.objects.all()
        cache.set(my_key, posts, 40)

    return posts


def post_find(post_id: int) -> Post:
    return Post.objects.get(id=post_id)

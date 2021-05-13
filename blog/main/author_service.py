from django.core.cache import cache

from main.models import Author


def author_all():
    my_key = Author.cache_key()
    if my_key in cache:
        posts = cache.get(my_key)
    else:
        posts = Author.objects.all()
        cache.set(my_key, posts, 40)

    return posts

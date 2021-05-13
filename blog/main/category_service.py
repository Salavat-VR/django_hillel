from django.core.cache import cache

from main.models import Category


def category_all():
    my_key = Category.cache_key()
    if my_key in cache:
        posts = cache.get(my_key)
    else:
        posts = Category.objects.all()
        cache.set(my_key, posts, 40)

    return posts

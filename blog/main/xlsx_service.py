from .models import Post


def get_simple_table_data():
    return Post.objects.all()

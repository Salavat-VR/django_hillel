from django.core.management import BaseCommand
from faker import Faker
from main.models import Author, Book, Category


class Command(BaseCommand):
    help = "generate random data"  # noqa

    def handle(self, *args, **kwargs):
        books_genres = ['Fantasy', 'Sci-Fi', 'Mystery', 'Thriller', 'Romance', 'Westerns', 'Dystopian',
                        'Contemporary']
        Author.objects.all().delete()
        faker = Faker()
        for _ in range(200):
            Author(name=faker.name(), email=faker.email()).save()
        for i in range(len(books_genres) - 1):
            Category(category_option=books_genres[i]).save()
        for i in range(400):
            author = Author.objects.order_by('?').first()
            category = Category.objects.order_by('?').first()
            Book(title=f'title {i}', author=author, category=category).save()

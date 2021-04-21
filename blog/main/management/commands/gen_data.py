from django.core.management import BaseCommand
from faker import Faker

from main.models import Author, Book


class Command(BaseCommand):
    help = "generate random data"  # noqa

    def handle(self, *args, **kwargs):
        Author.objects.all().delete()
        faker = Faker()
        for _ in range(200):
            Author(name=faker.name(), email=faker.email()).save()
        for i in range(400):
            author = Author.objects.order_by('?').first()
            Book(title=f'title {i}', author=author).save()

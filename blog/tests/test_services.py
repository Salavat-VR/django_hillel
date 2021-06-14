from main.author_service import author_all
from main.category_service import category_all
from main.logger_service import get_client_ip
from main.notify_service import periodic_email


def test_category_service(client):
    category_all()


def test_author_service(client):
    author_all()


def test_notify_service(client, faker_fixture):
    periodic_email(faker_fixture.email())

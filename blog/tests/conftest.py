import pytest
from faker import Faker
from pytest_django.fixtures import live_server


@pytest.fixture(autouse=True, scope='function')
def enable_db_access_for_all_tests(db):
    """
    giv access to DB for all tests
    """


@pytest.fixture(scope='function')
def my_first_fixture():
    yield 'I managed to do it'


@pytest.fixture(scope='function')
def faker_fixture():
    yield Faker()


@pytest.fixture(scope="session")
def my_live_server(request):
    request.getfixturevalue("my_first_fixture")
    return live_server(request)


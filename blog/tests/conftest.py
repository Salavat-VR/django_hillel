import pytest
from faker import Faker


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


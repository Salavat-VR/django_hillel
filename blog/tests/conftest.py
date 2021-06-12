import pytest


@pytest.fixture(autouse=True, scope='function')
def enable_db_access_for_all_tests(db):
    """
    giv access to DB for all tests
    """
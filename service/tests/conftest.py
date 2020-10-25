import pytest
from service import create_app


@pytest.fixture(scope="module")
def app():
    """ Create an instance of the App available for all tests"""
    return create_app()
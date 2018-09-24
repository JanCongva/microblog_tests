import pytest

from mt.base.application import Application


@pytest.fixture(scope="session")
def application():
    return Application(
        hostname="localhost:5000",
        scheme="http",
        username="misharov",
        password="123456"
    )

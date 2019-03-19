import pytest

from mt.base.application import Application


@pytest.fixture(scope="session")
def application():
    return Application(
        hostname="microblog:5000",
        scheme="http",
        username="user",
        password="123456"
    )

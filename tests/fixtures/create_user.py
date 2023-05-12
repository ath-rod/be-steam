import pytest
from services.users import UserService


@pytest.fixture
def create_user():
    def _create_user(username: str, password: str) -> dict:
        service = UserService()
        return service.create_user(username, password)

    return _create_user

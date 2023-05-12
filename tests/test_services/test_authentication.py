import pytest

# locals
from services.authentication import Authentication
from utils import random_str
from tests.fixtures import create_user


class TestAuthentication:
    service = Authentication()

    def test_authenticate_user(self, create_user):
        in_username = random_str(255)
        in_password = random_str(255)

        create_user(in_username, in_password)

        result = self.service.authenticate(in_username, in_password)
        assert result
        assert result["uuid"]
        assert result["created_at"]
        assert result["access_token"]
        assert result["expires_in"]

    def test_wrong_password(self, create_user):
        in_username = random_str(255)
        in_password = random_str(255)

        create_user(in_username, in_password)

        with pytest.raises(Exception):
            self.service.authenticate(in_username, "bad-password")

    def test_wrong_user(self):
        with pytest.raises(Exception):
            self.service.authenticate("bad-user", "bad-password")

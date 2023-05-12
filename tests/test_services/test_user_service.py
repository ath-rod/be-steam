import pytest
import uuid

# locals
from services.users import UserService
from tests.fixtures import drop_users
from utils import random_str


class TestUserService:
    service = UserService()

    def test_create_user(
        self,
    ):
        in_username = random_str(255)
        result = self.service.create_user(in_username, random_str(255))

        assert type(result) is dict
        assert "uuid" in result
        assert "username" in result
        assert "created_at" in result

        assert uuid.UUID(result["uuid"])
        assert result["username"] == in_username
        assert type(result["created_at"]) is str

    def test_create_duplicated(self):
        in_username = random_str(255)
        self.service.create_user(in_username, random_str(255))

        with pytest.raises(Exception):
            self.service.create_user(in_username, random_str(255))

    def test_get_users_default(self):
        for _ in range(100):
            self.service.create_user(random_str(255), random_str(255))

        result = self.service.get_users()
        assert type(result) is dict
        assert type(result["users"]) is list
        assert len(result["users"]) == 10

    def test_get_users_with_limit(self):
        n_users = 25
        limit = 20
        # gen 20 users
        for _ in range(n_users):
            self.service.create_user(random_str(255), random_str(255))

        result = self.service.get_users(limit=limit)

        assert type(result) is dict
        assert type(result["users"]) is list
        assert len(result["users"]) == limit

    def test_get_users_with_offset(self, drop_users):
        n_users = 20
        limit = 5

        for _ in range(n_users):
            self.service.create_user(random_str(255), random_str(255))

        result = self.service.get_users(limit=limit)
        assert len(result["users"]) == 5

        result = self.service.get_users(limit=limit, offset=10)
        assert len(result["users"]) == 5

        result = self.service.get_users(limit=limit, offset=15)
        assert len(result["users"]) == 5

        result = self.service.get_users(limit=limit, offset=19)
        assert len(result["users"]) == 1

    def test_get_users_with_search_str(self):
        bucket = [random_str(255) for _ in range(20)]

        for in_username in bucket:
            self.service.create_user(in_username, random_str(255))

        result = self.service.get_users(search_str=bucket[0])
        fail = self.service.get_users(search_str="non-existent")

        assert len(result["users"]) == 1
        assert len(fail["users"]) == 0

# locals
from config import logging
from dao.users import get_users, insert_user
from utils.exceptions import ConstraintError


class UserService:
    __all__ = ["create_user", "get_users"]

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(cls, UserService).__new__(cls)
        return cls.instance

    def create_user(self, username: str, password: str) -> dict:
        logging.info("attemting to generate a new user record")

        # Read from users to check whether is possible to write
        users = get_users(limit=1000, offset=0, search_str=username)

        if len(users) > 0:
            raise ConstraintError(
                msg="UniqueConstraintViolation",
                errors=["username may be already taken"],
            )

        result = insert_user(username, password)

        # unpackage raw psycopg tuple
        users = list(map(self._map_raw_tuple, result))

        return users[0]

    def get_users(
        self, search_str: str = None, limit: int = 10, offset: int = 0
    ) -> dict:
        logging.info(
            f"""
        loading users with options:
        limit: {limit}
        offset: {offset}
        search_str: {search_str}
        """
        )

        result = get_users(limit, offset, search_str)
        users = list(map(self._map_raw_tuple, result))
        return dict(users=users)

    @staticmethod
    def _map_raw_tuple(item: tuple) -> dict:
        uuid, username, created_at = item
        return dict(uuid=uuid, username=username, created_at=str(created_at))

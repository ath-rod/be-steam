from jwt import encode, decode
from datetime import datetime

# locals
from dao.users import check_password, get_users
from config import logging, env
from utils.exceptions import ConstraintError


class Authentication:
    __all__ = []

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(cls, Authentication).__new__(cls)
        return cls.instance

    def authenticate(self, username: str, password: str) -> dict:
        logging.info("authenticating new user")

        user_result = get_users(1, 0, username)
        if not user_result:
            raise ConstraintError(msg="Unauthorized", code=401, errors=["Unauthorized"])

        uuid, _, created_at = user_result[0]

        if not self._check_password(username, password):
            raise ConstraintError(msg="Unauthorized", code=401, errors=["Unauthorized"])

        access_token = self._gen_access_token(
            dict(
                uuid=uuid,
                created_at=str(datetime.now()),
            )
        )

        return dict(
            uuid=uuid,
            expires_in=env.JWT_EXPIRES_IN,
            created_at=str(datetime.now()),
            access_token=access_token,
        )

    @staticmethod
    def _check_password(username: str, password: str) -> bool:
        result = check_password(username, password)
        return result

    @staticmethod
    def _gen_access_token(data: dict) -> str:
        data = {**data, **{"expires_in": env.JWT_EXPIRES_IN}}
        return encode(data, env.JWT_SECRET, algorithm=env.JWT_ALGORITHM)

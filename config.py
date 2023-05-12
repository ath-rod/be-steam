import logging
from os import getenv
from configparser import ConfigParser

# Collect environment variable
__ENV__ = getenv("ENV") or "development"

# Built TOML parser
config = ConfigParser()
config.read("config.ini")

# Initialize app logger
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO
)


class env:  # lower case for usare readability
    """
    Application config wrapper
    collecting ConfigParser TOML
    output.
    """

    SESSION_SECRET = config.get(__ENV__, "session_secret")
    HOST = config.get(__ENV__, "host")
    PORT = config.getint(__ENV__, "port")
    DB_NAME = config.get(__ENV__, "db_name")
    DB_USER = config.get(__ENV__, "db_user")
    DB_PASSWORD = config.get(__ENV__, "db_password")
    DB_HOST = config.get(__ENV__, "db_host")
    DB_PORT = config.getint(__ENV__, "db_port")
    JWT_SECRET = config.get(__ENV__, "jwt_secret")
    JWT_EXPIRES_IN = config.getint(__ENV__, "jwt_expires_in")
    JWT_REFRESH_EXPIRES_IN = config.getint(__ENV__, "jwt_refresh_expires_in")
    JWT_ALGORITHM = config.get(__ENV__, "jwt_algorithm")

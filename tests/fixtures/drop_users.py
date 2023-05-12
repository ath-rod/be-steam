import pytest
from database import connection


@pytest.fixture
def drop_users():
    return connection.pool.execute("""DELETE FROM USERS;""")

from config import env
from .connection import Connection

# Very simple singleton expression
connection = None

if not connection:
    connection = Connection(
        database=env.DB_NAME,
        user=env.DB_USER,
        password=env.DB_PASSWORD,
        host=env.DB_HOST,
        port=env.DB_PORT,
    )

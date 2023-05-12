import psycopg2
from config import logging


class Connection:
    def __init__(
        self, database: str, user: str, password: str, host: str, port: str
    ) -> "Connection":
        self.database = database
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None
        self.pool = None

        # Initialize connection
        self._connect()
        self._setup()

    def _connect(self) -> None:
        if not self.pool:
            logging.info("Building-up fresh connection pool")
            self.conn = psycopg2.connect(
                dbname=self.database,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
            )

    def _setup(self) -> None:
        self.conn.autocommit = True
        self.pool = self.conn.cursor()

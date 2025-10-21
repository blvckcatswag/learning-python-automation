import os
import logging
import psycopg2
from psycopg2 import sql, OperationalError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Database:
    def __init__(self):
        self.host = os.getenv("POSTGRES_HOST", "localhost")
        self.port = int(os.getenv("POSTGRES_PORT", 5432))
        self.database = os.getenv("POSTGRES_DB", "testdb")
        self.user = os.getenv("POSTGRES_USER", "postgres")
        self.password = os.getenv("POSTGRES_PASSWORD", "postgres")
        self.conn = None

    def connect(self) -> bool:
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                dbname=self.database,
                user=self.user,
                password=self.password,
                connect_timeout=5
            )
            self.conn.autocommit = True
            logger.info("Connected to Postgres at %s:%s", self.host, self.port)
            return True
        except OperationalError as e:
            logger.error("Connection failed: %s", e)
            return False

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    def create_table(self):
        q = """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            age INT NOT NULL
        );
        """
        with self.conn.cursor() as cur:
            cur.execute(q)

    def insert_user(self, name: str, age: int) -> int:
        q = "INSERT INTO users(name, age) VALUES (%s, %s) RETURNING id;"
        with self.conn.cursor() as cur:
            cur.execute(q, (name, age))
            uid = cur.fetchone()[0]
            return uid

    def update_user_age(self, user_id: int, age: int) -> None:
        q = "UPDATE users SET age = %s WHERE id = %s;"
        with self.conn.cursor() as cur:
            cur.execute(q, (age, user_id))

    def delete_user(self, user_id: int) -> None:
        q = "DELETE FROM users WHERE id = %s;"
        with self.conn.cursor() as cur:
            cur.execute(q, (user_id,))

    def get_user(self, user_id: int):
        q = "SELECT id, name, age FROM users WHERE id = %s;"
        with self.conn.cursor() as cur:
            cur.execute(q, (user_id,))
            return cur.fetchone()

    def list_users(self):
        q = "SELECT id, name, age FROM users ORDER BY id;"
        with self.conn.cursor() as cur:
            cur.execute(q)
            return cur.fetchall()

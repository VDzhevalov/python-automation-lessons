import time
import pytest
import psycopg2
from psycopg2 import OperationalError

DB = dict(
    dbname="test_db",
    user="test_user",
    password="test_password",
    host="db",
    port=5432,
)

def _connect_with_retry(retries=30, delay=1.0):
    last = None
    for _ in range(retries):
        try:
            return psycopg2.connect(**DB)
        except OperationalError as e:
            last = e
            time.sleep(delay)
    raise last

@pytest.fixture(scope="session")
def db_conn():
    conn = _connect_with_retry()
    yield conn
    conn.close()

@pytest.fixture(autouse=True, scope="session")
def ensure_schema(db_conn):
    cur = db_conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
          id   INT PRIMARY KEY,
          name TEXT NOT NULL
        )
    """)
    db_conn.commit()

@pytest.fixture(autouse=True)
def clean_users(db_conn):
    cur = db_conn.cursor()
    cur.execute("DELETE FROM users")
    db_conn.commit()
    yield
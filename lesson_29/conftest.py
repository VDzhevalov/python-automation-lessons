# tests/conftest.py
import pytest, psycopg2

def _conn():
    return psycopg2.connect(
        dbname="test_db",
        user="test_user",
        password="test_password",
        host="db",
        port="5432"
    )

@pytest.fixture(autouse=True, scope="session")
def ensure_schema():
    with _conn() as conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
              id   INT PRIMARY KEY,
              name TEXT NOT NULL
            );
        """)
        conn.commit()

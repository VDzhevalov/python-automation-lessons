import psycopg2

DB = dict(
    dbname="test_db",
    user="test_user",
    password="test_password",
    host="db",
    port=5432,
)

def _conn():
    return psycopg2.connect(**DB)

def test_database_connection():
    with _conn() as conn:
        assert conn is not None

def test_data_insertion():
    with _conn() as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO users (id, name) VALUES (%s, %s)", (1, "John"))
        conn.commit()
        cur.execute("SELECT name FROM users WHERE id=%s", (1,))
        (name,) = cur.fetchone()
        assert name == "John"

def test_data_update():
    with _conn() as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO users (id, name) VALUES (%s, %s)", (2, "Jane"))
        conn.commit()

        cur.execute("UPDATE users SET name=%s WHERE id=%s", ("Bill", 2))
        conn.commit()

        cur.execute("SELECT name FROM users WHERE id=%s", (2,))
        (name,) = cur.fetchone()
        assert name == "Bill"

def test_data_delete():
    with _conn() as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO users (id, name) VALUES (%s, %s)", (3, "For Delete"))
        conn.commit()

        cur.execute("DELETE FROM users WHERE id=%s", (3,))
        conn.commit()

        cur.execute("SELECT COUNT(*) FROM users WHERE id=%s", (3,))
        (cnt,) = cur.fetchone()
        assert cnt == 0
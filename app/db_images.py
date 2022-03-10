import os
import sqlite3

conn = sqlite3.connect(os.path.join("db", "images.db"))
cursor = conn.cursor()


def _init_db() -> None:
    """database initialization"""
    file = os.path.join("db", "createdb.sql")
    with open(file, "r") as f:
        sql = f.read()
    cursor.executescript(sql)
    conn.commit()


def check_db_exists() -> None:
    """checks db initialization, if not — makes initialization"""
    cursor.execute("SELECT name FROM sqlite_master "
                   "WHERE type='table' AND name='reminder'")
    table_exists = cursor.fetchall()
    if table_exists:
        return
    _init_db()


check_db_exists()

import sqlite3
from contextlib import contextmanager

sqlite_file_name = "school.db"

@contextmanager
def get_db_connection():
    conn = sqlite3.connect(sqlite_file_name)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()








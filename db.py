# db.py

import sqlite3
from contextlib import contextmanager
import os

@contextmanager
def get_db():
    db_path = os.path.join(os.path.dirname(__file__), "database.db")
    connection = sqlite3.connect(db_path, check_same_thread=False)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    try:
        yield cursor
        connection.commit()
    except sqlite3.Error as e:
        print(f"Database Error: {e}")
        connection.rollback()
    finally:
        connection.close()

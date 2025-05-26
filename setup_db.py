import sqlite3

def setup_db():
    with sqlite3.connect("habit_tracker.db") as conn:
        cursor = conn.cursor()
        
        # Create habits table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS habits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            category TEXT,
            user TEXT
        )
        """)
        
        # Create completions table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS completions (
            id INTEGER PRIMARY KEY,
            habit_id INTEGER,
            completed_at TEXT,
            FOREIGN KEY (habit_id) REFERENCES habits(id)
        )
        """)
        conn.commit()

setup_db()

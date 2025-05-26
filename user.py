# user.py
from db import get_db
from utils import get_habit_completions, calculate_streak
from datetime import datetime

class User:
    def __init__(self, username):
        self.username = username
        self.habits_cache = None

    def get_habits(self):
        if not self.habits_cache:
            with get_db() as db:
                self.habits_cache = db.execute(
                    "SELECT id, name, category FROM habits WHERE user = ?",
                    (self.username,)
                ).fetchall()
        return self.habits_cache

    def add_habit(self, habit_name, category):
        if not habit_name.strip():
            raise ValueError("Habit name cannot be empty.")

        with get_db() as db:
            db.execute(
                "INSERT INTO habits (name, category, user) VALUES (?, ?, ?)",
                (habit_name, category, self.username)
            )
        self.habits_cache = None  # Clear cache to refresh list

    def delete_habit(self, habit_id):
        with get_db() as db:
            db.execute("DELETE FROM habits WHERE id = ? AND user = ?", (habit_id, self.username))
            db.execute("DELETE FROM completions WHERE habit_id = ?", (habit_id,))
        self.habits_cache = None  # Clear cache to refresh list

    def complete_habit(self, habit_id):
        """
        Marks a habit as completed with a timestamp.
        """
        with get_db() as db:
            db.execute(
                "INSERT INTO completions (habit_id, completed_at) VALUES (?, ?)",
                (habit_id, datetime.now().isoformat())
            )
        self.habits_cache = None  # Clear cache to refresh list

    def get_streak(self, habit_id, frequency="Daily"):
        completions = get_habit_completions(habit_id)
        return calculate_streak(completions, frequency)

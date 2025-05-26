# analytics.py
from db import get_db

def get_longest_streak(username, category="Daily"):
    query = "SELECT h.name, MAX(streak) as max_streak FROM (SELECT h.name, COUNT(c.id) as streak FROM habits h LEFT JOIN completions c ON h.id = c.habit_id WHERE h.user = ? AND h.category = ? GROUP BY h.name) as streaks GROUP BY h.name ORDER BY max_streak DESC LIMIT 1;" 
    with get_db() as db:
        result = db.execute(query, (username, category)).fetchone() 
        return result if result else ("No habits found", 0)


# utils.py
from db import get_db
from datetime import datetime, timedelta

def get_habit_completions(habit_id):
    """
    Retrieves all completions for a specific habit.
    """
    with get_db() as db:
        completions = db.execute(
            "SELECT completed_at FROM completions WHERE habit_id = ? ORDER BY completed_at ASC",
            (habit_id,)
        ).fetchall()
    return [completion["completed_at"] for completion in completions]

def calculate_streak(completions, frequency="Daily"):
    """
    Calculates the streak for a habit based on its frequency (Daily, Weekly, Monthly).
    """
    if not completions:
        return 0

    streak = 0
    current_streak = 0
    last_date = None

    for completion in completions:
        date = datetime.fromisoformat(completion)

        if not last_date:
            current_streak = 1
        else:
            difference = date - last_date

            if frequency == "Daily" and difference.days == 1:
                current_streak += 1
            elif frequency == "Weekly" and difference.days <= 7:
                current_streak += 1
            elif frequency == "Monthly" and difference.days <= 31:
                current_streak += 1
            else:
                current_streak = 1  # Streak breaks

        last_date = date
        streak = max(streak, current_streak)

    return streak

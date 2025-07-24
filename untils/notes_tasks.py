from collections import defaultdict
import time

user_notes = defaultdict(list)
user_tasks = defaultdict(list)
user_reminders = defaultdict(list)

def add_note(user_id: int, note: str):
    user_notes[user_id].append(note)

def get_notes(user_id: int):
    return user_notes[user_id]

def clear_notes(user_id: int):
    user_notes[user_id] = []

def add_task(user_id: int, task: str):
    user_tasks[user_id].append(task)

def get_tasks(user_id: int):
    return user_tasks[user_id]

def clear_tasks(user_id: int):
    user_tasks[user_id] = []

def add_reminder(user_id: int, text: str, remind_time: int):
    reminder = {
        "text": text,
        "time": remind_time,
        "added": int(time.time())
    }
    user_reminders[user_id].append(reminder)

def get_due_reminders(user_id: int):
    now = int(time.time())
    due = []
    remaining = []
    for r in user_reminders[user_id]:
        if now >= r["time"]:
            due.append(r)
        else:
            remaining.append(r)
    user_reminders[user_id] = remaining
    return due

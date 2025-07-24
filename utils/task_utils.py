import json
import os

TASKS_FILE = "data/tasks.json"


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return {}
    with open(TASKS_FILE, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}


def save_tasks(tasks):
    os.makedirs(os.path.dirname(TASKS_FILE), exist_ok=True)
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)


def add_task(user_id: int, task: str):
    tasks = load_tasks()
    uid = str(user_id)
    if uid not in tasks:
        tasks[uid] = []
    tasks[uid].append(task)
    save_tasks(tasks)


def remove_task(user_id: int, index: int):
    tasks = load_tasks()
    uid = str(user_id)
    if uid in tasks and 0 <= index < len(tasks[uid]):
        removed = tasks[uid].pop(index)
        save_tasks(tasks)
        return removed
    return None


def list_tasks(user_id: int):
    tasks = load_tasks()
    return tasks.get(str(user_id), [])


def clear_tasks(user_id: int):
    tasks = load_tasks()
    uid = str(user_id)
    if uid in tasks:
        del tasks[uid]
        save_tasks(tasks)
        return True
    return False

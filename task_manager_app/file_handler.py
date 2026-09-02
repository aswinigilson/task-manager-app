import json
from pathlib import Path
from .task import Task


TASKS_FILE = Path("data") / "tasks.json"


def read_tasks():
    try:
        if not TASKS_FILE.exists():
            return []

        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            print("Error: Task data must be a list.")
            return []

        return [Task.from_dict(item) for item in data]

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Error: tasks.json is corrupted.")
        return []

    except (KeyError, TypeError):
        print("Error: Invalid task data.")
        return []

    except OSError as error:
        print(f"File error: {error}")
        return []


def write_tasks(tasks):
    try:
        TASKS_FILE.parent.mkdir(parents=True, exist_ok=True)

        data = [task.to_dict() for task in tasks]

        with open(TASKS_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        return True

    except OSError as error:
        print(f"Error saving tasks: {error}")
        return False
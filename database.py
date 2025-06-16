import json
import os
from task import Task

class TaskDatabase:
    TASKS_FILE = "tasks.json"

    def load_tasks(self):
        if os.path.exists(self.TASKS_FILE):
            with open(self.TASKS_FILE, "r") as file:
                tasks_data = json.load(file)
                return [Task(**data) for data in tasks_data]
        return []

    def save_tasks(self, tasks):
        with open(self.TASKS_FILE, "w") as file:
            json.dump([task.to_dict() for task in tasks], file, indent=4)

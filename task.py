class Task:
    def __init__(self, id, title, desc="", due="", priority="low", completed=False):
        self.id = id
        self.title = title
        self.desc = desc
        self.due = due
        self.priority = priority
        self.completed = completed

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "desc": self.desc,
            "due": self.due,
            "priority": self.priority,
            "completed": self.completed
        }

    def mark_complete(self):
        self.completed = True

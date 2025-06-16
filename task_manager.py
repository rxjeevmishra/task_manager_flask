import sqlite3

class TaskManager:
    def __init__(self, db_path='tasks.db'):
        self.db_path = db_path

    def connect(self):
        return sqlite3.connect(self.db_path)

    def list_tasks(self):
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM tasks")
        rows = cur.fetchall()
        conn.close()
        return [
            {
                "id": row[0],
                "title": row[1],
                "desc": row[2],
                "due": row[3],
                "priority": row[4],
                "completed": bool(row[5])
            }
            for row in rows
        ]

    def add_task(self, title, desc, due, priority):
        conn = self.connect()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO tasks (title, desc, due, priority) VALUES (?, ?, ?, ?)",
            (title, desc, due, priority)
        )
        conn.commit()
        conn.close()

    def complete_task(self, task_id):
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
        conn.commit()
        conn.close()

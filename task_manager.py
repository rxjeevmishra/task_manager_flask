import sqlite3

class TaskManager:
    def __init__(self, db_path='tasks.db'):
        self.db_path = db_path
        self._create_table_if_not_exists()

    def connect(self):
        return sqlite3.connect(self.db_path)

    def _create_table_if_not_exists(self):
        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute('''
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    desc TEXT,
                    due DATE,
                    priority TEXT,
                    completed INTEGER DEFAULT 0
                )
            ''')
            conn.commit()

    def list_tasks(self):
        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM tasks")
            rows = cur.fetchall()
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
        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO tasks (title, desc, due, priority) VALUES (?, ?, ?, ?)",
                (title, desc, due, priority)
            )
            conn.commit()

    def complete_task(self, task_id):
        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
            conn.commit()
    
    def delete_task(self, task_id):
        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
            conn.commit()
    
    def get_task(self, task_id):
        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
            row = cur.fetchone()
            if row:
                return {
                    'id': row[0],
                    'title': row[1],
                    'desc': row[2],
                    'due': row[3],
                    'priority': row[4],
                    'completed': row[5]
                }
            return None

    def update_task(self, task_id, title, desc, due, priority):
        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute("UPDATE tasks SET title=?, desc=?, due=?, priority=? WHERE id=?",
                        (title, desc, due, priority, task_id))
            conn.commit()

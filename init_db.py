import sqlite3

conn = sqlite3.connect("tasks.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    desc TEXT,
    due TEXT,
    priority TEXT,
    completed INTEGER DEFAULT 0
)
""")

conn.commit()
conn.close()


import sqlite3

DB_NAME = "campusconnect.db"


def create_connection():
    return sqlite3.connect(DB_NAME)


def create_table():
    with create_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                subject TEXT NOT NULL,
                task_type TEXT NOT NULL,
                completed INTEGER DEFAULT 0,
                due_date TEXT
            )
        """)


def add_task(title, subject, task_type, due_date=None):
    with create_connection() as connection:
        connection.execute("""
            INSERT INTO tasks
            (title, subject, task_type, completed, due_date)
            VALUES (?, ?, ?, 0, ?)
        """, (title, subject, task_type, due_date))


def get_tasks():
    with create_connection() as connection:
        cursor = connection.execute("""
            SELECT id, title, subject, task_type, completed, due_date
            FROM tasks
            ORDER BY id DESC
        """)
        return cursor.fetchall()


def mark_completed(task_id):
    with create_connection() as connection:
        connection.execute("""
            UPDATE tasks
            SET completed = 1
            WHERE id = ?
        """, (task_id,))


def update_task(task_id, title, subject, task_type, due_date):
    with create_connection() as connection:
        connection.execute("""
            UPDATE tasks
            SET title = ?,
                subject = ?,
                task_type = ?,
                due_date = ?
            WHERE id = ?
        """, (title, subject, task_type, due_date, task_id))


def delete_task(task_id):
    with create_connection() as connection:
        connection.execute(
            "DELETE FROM tasks WHERE id = ?",
            (task_id,)
        )


from contextlib import contextmanager
import sqlite3

DB_NAME = "campusconnect.db"


@contextmanager
def create_connection():
    connection = sqlite3.connect(DB_NAME)
    try:
        yield connection
        connection.commit()
    except BaseException:
        connection.rollback()
        raise
    finally:
        connection.close()


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


def add_sample_tasks():
    """Add sample tasks once without duplicating their titles."""

    sample_tasks = [
        # Previous completed tasks
        ("Python Basics Assignment", "Python", "Assignment",
         "2026-10-01", 1),
        ("Excel Dashboard", "Excel", "Project",
         "2026-10-03", 1),
        ("SQL Queries Practice", "SQL", "Assignment",
         "2026-10-05", 1),
        ("Python Loops Practice", "Python", "Assignment",
         "2026-10-06", 1),
        ("Data Cleaning Exercise", "Excel", "Assignment",
         "2026-10-07", 1),
        ("Power BI Basics", "Power BI", "Assignment",
         "2026-10-08", 1),
        ("Database Design", "SQL", "Project",
         "2026-10-09", 1),
        ("Python Functions Practice", "Python", "Assignment",
         "2026-10-10", 1),

        # Upcoming pending tasks
        ("Python OOPs Project", "Python", "Project",
         "2026-10-15", 0),
        ("Power BI Sales Dashboard", "Power BI", "Project",
         "2026-10-17", 0),
        ("SQL Joins Practice", "SQL", "Assignment",
         "2026-10-18", 0),
        ("Student Management System", "Python", "Project",
         "2026-10-20", 0),
        ("Excel Advanced Formulas", "Excel", "Assignment",
         "2026-10-21", 0),
        ("Data Analysis Report", "Python", "Project",
         "2026-10-23", 0),
        ("CampusConnect Testing", "Python", "Assignment",
         "2026-10-25", 0),
        ("Final Project Documentation", "Python", "Project",
         "2026-10-28", 0),
    ]

    with create_connection() as connection:
        for title, subject, task_type, due_date, completed in sample_tasks:
            existing = connection.execute(
                "SELECT id FROM tasks WHERE title = ?",
                (title,)
            ).fetchone()

            if existing is None:
                connection.execute("""
                    INSERT INTO tasks
                    (title, subject, task_type, completed, due_date)
                    VALUES (?, ?, ?, ?, ?)
                """, (
                    title, subject, task_type, completed, due_date
                ))


if __name__ == "__main__":
    create_table()
    add_sample_tasks()
    print("Sample tasks added successfully!")

    tasks = get_tasks()
    print("Total tasks:", len(tasks))

    for task in tasks:
        task_id, title, subject, task_type, completed, due_date = task
        status = "Completed" if completed else "Pending"
        print(f"{title} | Due: {due_date} | {status}")

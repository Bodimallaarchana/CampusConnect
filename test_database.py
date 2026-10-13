
from database import create_table, add_task, get_tasks


create_table()

add_task(
    "Complete Python project",
    "Python",
    "Assignment"
)

tasks = get_tasks()

print("===== SAVED STUDENT TASKS =====")

for task in tasks:
    print(task)

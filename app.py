
import csv
from io import StringIO

import streamlit as st
from datetime import date, timedelta
from models import AssignmentTask, StudyTask
from database import (
    add_task,
    create_table,
    delete_task,
    get_tasks,
    mark_completed,
    update_task,
)


st.set_page_config(
    page_title="CampusConnect",
    page_icon="🎓",
    layout="wide"
)

create_table()

st.title("🎓 CampusConnect")
st.caption("Smart College Student Assistant")

st.subheader("➕ Add a New Task")

with st.form("task_form"):
    title = st.text_input("Task Title")
    subject = st.text_input("Subject")

    task_type = st.selectbox(
        "Task Type",
        ["Assignment", "Study Session"]
    )

    due_date = st.date_input(
        "Due Date",
        value=date.today() + timedelta(days=1),
        min_value=date.today()
    )

    submitted = st.form_submit_button("Add Task")

    if submitted:
        if title.strip() and subject.strip():
            add_task(
                title.strip(),
                subject.strip(),
                task_type,
                due_date.isoformat()
            )
            st.success("Task added successfully!")
            st.rerun()
        else:
            st.warning("Enter both the task title and subject.")

st.divider()

tasks = get_tasks()

total = len(tasks)
completed = sum(task[4] == 1 for task in tasks)
pending = total - completed

col1, col2, col3 = st.columns(3)
col1.metric("Total Tasks", total)
col2.metric("Completed", completed)
col3.metric("Pending", pending)

st.subheader("📊 Task Progress Dashboard")
if total > 0:
    chart_data = {
        "Status": ["Completed", "Pending"],
        "Count": [completed, pending],
    }
    st.bar_chart(
        chart_data,
        x="Status",
        y="Count",
        color="Status",
    )
    progress = completed / total
    st.write("Overall completion progress")
    st.progress(progress)
    st.write(f"{progress:.0%} of your tasks completed")
else:
    st.info("Add your first task to see your progress dashboard.")

csv_buffer = StringIO()
csv_writer = csv.writer(csv_buffer)
csv_writer.writerow(
    ["task_id", "title", "subject", "task_type", "completed", "due_date", "status"]
)
for task in tasks:
    task_id, task_title, task_subject, task_type, is_completed, task_due_date = task
    if is_completed:
        task_status = "Completed"
    elif task_due_date and date.fromisoformat(task_due_date) < date.today():
        task_status = "Overdue"
    else:
        task_status = "Pending"
    csv_writer.writerow(
        [task_id, task_title, task_subject, task_type, is_completed, task_due_date, task_status]
    )

st.download_button(
    "Export tasks for Power BI (CSV)",
    data=csv_buffer.getvalue(),
    file_name="campusconnect_tasks.csv",
    mime="text/csv",
)

st.subheader("🗓️ Weekly Study Planner")
today = date.today()
week_start = today - timedelta(days=today.weekday())
week_end = week_start + timedelta(days=6)
st.caption(
    f"Week of {week_start.strftime('%d %b')}–{week_end.strftime('%d %b %Y')}"
)

weekly_schedule = {
    week_start + timedelta(days=offset): []
    for offset in range(7)
}

for task in tasks:
    due_date_text = task[5]
    if due_date_text:
        task_due_date = date.fromisoformat(due_date_text)
        if week_start <= task_due_date <= week_end:
            weekly_schedule[task_due_date].append(task)

for planner_date, day_tasks in weekly_schedule.items():
    with st.container(border=True):
        st.markdown(f"**{planner_date.strftime('%A, %d %b')}**")
        if day_tasks:
            for task in day_tasks:
                _, task_title, task_subject, task_type, is_completed, _ = task
                if is_completed:
                    status_icon = "✅"
                elif planner_date < today:
                    status_icon = "⚠️"
                else:
                    status_icon = "🔹"
                st.write(
                    f"{status_icon} {task_title} — {task_subject} · {task_type}"
                )
        else:
            st.caption("No tasks scheduled")

st.divider()
st.subheader("🔎 Find Your Tasks")

search_text = st.text_input("Search by title or subject")

type_filter = st.selectbox(
    "Task Type",
    ["All", "Assignment", "Study Session"]
)

status_filter = st.selectbox(
    "Status",
    ["All", "Pending", "Completed", "Overdue"]
)

filtered_tasks = []

for task in tasks:
    task_id, title, subject, task_type, is_completed, due_date = task

    search = search_text.strip().lower()
    matches_search = (
        search in title.lower()
        or search in subject.lower()
    )

    matches_type = (
        type_filter == "All"
        or task_type == type_filter
    )

    is_overdue = (
        not is_completed
        and due_date is not None
        and date.fromisoformat(due_date) < date.today()
    )

    matches_status = (
        status_filter == "All"
        or (status_filter == "Pending" and is_completed == 0)
        or (status_filter == "Completed" and is_completed == 1)
        or (status_filter == "Overdue" and is_overdue)
    )

    if matches_search and matches_type and matches_status:
        filtered_tasks.append(task)

st.subheader("📚 My Tasks")
st.write(f"Showing {len(filtered_tasks)} task(s)")

if filtered_tasks:
    for task in filtered_tasks:
        task_id, title, subject, task_type, is_completed, due_date = task

        with st.container(border=True):
            st.write(f"**{title}**")
            if task_type == "Assignment":
                task_object = AssignmentTask(title, subject)
            else:
                task_object = StudyTask(title, subject)
            st.write(task_object.describe())

            if due_date:
                due = date.fromisoformat(due_date)
                st.write(f"Due date: {due.strftime('%d %b %Y')}")

                if not is_completed and due < date.today():
                    st.error("⚠️ Overdue! This task needs attention.")
                elif not is_completed and due == date.today():
                    st.warning("Due today!")
                elif not is_completed:
                    st.info(f"{(due - date.today()).days} day(s) remaining")

            if is_completed:
                st.success("Status: Completed")
            else:
                st.warning("Status: Pending")
                if st.button("Mark Completed", key=f"done_{task_id}"):
                    mark_completed(task_id)
                    st.rerun()

            with st.expander("✏️ Edit or 🗑️ Delete Task"):
                with st.form(f"edit_form_{task_id}"):
                    new_title = st.text_input(
                        "Task Title",
                        value=title,
                        key=f"title_{task_id}"
                    )
                    new_subject = st.text_input(
                        "Subject",
                        value=subject,
                        key=f"subject_{task_id}"
                    )
                    task_types = ["Assignment", "Study Session", "Project"]
                    new_type = st.selectbox(
                        "Task Type",
                        task_types,
                        index=task_types.index(task_type),
                        key=f"type_{task_id}"
                    )
                    new_due_date = st.date_input(
                        "Due Date",
                        value=date.fromisoformat(due_date) if due_date else date.today(),
                        key=f"date_{task_id}"
                    )

                    save_edit = st.form_submit_button("Save Changes")

                    if save_edit:
                        if new_title.strip() and new_subject.strip():
                            update_task(
                                task_id,
                                new_title.strip(),
                                new_subject.strip(),
                                new_type,
                                new_due_date.isoformat()
                            )
                            st.success("Task updated successfully!")
                            st.rerun()
                        else:
                            st.warning("Enter both title and subject.")

                if st.button("🗑️ Delete Task", key=f"delete_{task_id}"):
                    delete_task(task_id)
                    st.success("Task deleted successfully!")
                    st.rerun()
else:
    st.info("No tasks match your filters.")


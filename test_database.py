
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import database


class DatabaseTests(unittest.TestCase):
    def setUp(self):
        temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(temporary_directory.cleanup)

        database_name = Path(temporary_directory.name) / "campusconnect.db"
        database_patch = patch.object(database, "DB_NAME", str(database_name))
        database_patch.start()
        self.addCleanup(database_patch.stop)

        database.create_table()

    def test_add_task(self):
        database.add_task(
            "Complete Python project",
            "Python",
            "Assignment",
            "2026-10-15",
        )

        tasks = database.get_tasks()

        self.assertEqual(len(tasks), 1)
        self.assertEqual(
            tasks[0][1:],
            ("Complete Python project", "Python", "Assignment", 0, "2026-10-15"),
        )

    def test_update_completion_and_delete_task(self):
        database.add_task("Study Python", "Python", "Study Session")
        task_id = database.get_tasks()[0][0]

        database.mark_completed(task_id)
        database.update_task(
            task_id,
            "Review Python",
            "Python",
            "Project",
            "2026-10-20",
        )

        self.assertEqual(
            database.get_tasks(),
            [(task_id, "Review Python", "Python", "Project", 1, "2026-10-20")],
        )

        database.delete_task(task_id)
        self.assertEqual(database.get_tasks(), [])


if __name__ == "__main__":
    unittest.main()

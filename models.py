
class Task:
    def __init__(self, title, subject):
        self.title = title
        self.subject = subject

    def describe(self):
        return f"Task: {self.title} | Subject: {self.subject}"


class AssignmentTask(Task):
    def describe(self):
        return f"Assignment: {self.title} | Subject: {self.subject}"


class StudyTask(Task):
    def describe(self):
        return f"Study Session: {self.title} | Subject: {self.subject}"

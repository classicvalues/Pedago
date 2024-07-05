# pedago/user/student.py

from .user import User

class Student(User):
    def __init__(self, user_id: str, name: str, email: str, password: str):
        super().__init__(user_id, name, email, password, role="student")
        self.progress = {}
        self.completed_courses = []

    def updateProgress(self, course_id: str, lesson_id: str, progress: float):
        """Updates student's progress in a course."""
        if course_id not in self.progress:
            self.progress[course_id] = {}
        self.progress[course_id][lesson_id] = progress

    def completeCourse(self, course_id: str):
        """Marks a course as completed by the student."""
        if course_id not in self.completed_courses:
            self.completed_courses.append(course_id)

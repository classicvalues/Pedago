from .instructor import Instructor
from typing import List

class TeacherManager:
    def __init__(self):
        self.teachers = {}

    def addTeacher(self, teacher_id: str, teacher: Instructor) -> bool:
        """Adds a new teacher to the system."""
        if teacher_id not in self.teachers:
            self.teachers[teacher_id] = teacher
            return True
        return False

    def updateTeacherDetails(self, teacher_id: str, name: str = None, email: str = None) -> bool:
        """Updates teacher details."""
        if teacher_id in self.teachers:
            teacher = self.teachers[teacher_id]
            if name:
                teacher.updateName(name)
            if email:
                teacher.updateEmail(email)
            return True
        return False

    def getTeacher(self, teacher_id: str) -> Instructor:
        """Retrieves a teacher by their ID."""
        return self.teachers.get(teacher_id, None)

    def listTeachers(self) -> List[Instructor]:
        """Lists all teachers."""
        return list(self.teachers.values())

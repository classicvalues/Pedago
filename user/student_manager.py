from .student import Student
from typing import List

class StudentManager:
    def __init__(self):
        self.students = {}

    def addStudent(self, student_id: str, student: Student) -> bool:
        """Adds a new student to the system."""
        if student_id not in self.students:
            self.students[student_id] = student
            return True
        return False

    def updateStudentDetails(self, student_id: str, name: str = None, email: str = None) -> bool:
        """Updates student details."""
        if student_id in self.students:
            student = self.students[student_id]
            if name:
                student.updateName(name)
            if email:
                student.updateEmail(email)
            return True
        return False

    def getStudent(self, student_id: str) -> Student:
        """Retrieves a student by their ID."""
        return self.students.get(student_id, None)

    def listStudents(self) -> List[Student]:
        """Lists all students."""
        return list(self.students.values())

from .user import StudentManager  # Importing main implementations from user.py

class StudentManagerWrapper:
    def __init__(self):
        self.student_manager = StudentManager()

    def addStudent(self, student_id: str, name: str, email: str) -> bool:
        return self.student_manager.addStudent(student_id, name, email)

    def removeStudent(self, student_id: str) -> bool:
        return self.student_manager.removeStudent(student_id)

    def getStudent(self, student_id: str) -> dict:
        return self.student_manager.getStudent(student_id)

    def listStudents(self) -> List[dict]:
        return self.student_manager.listStudents()



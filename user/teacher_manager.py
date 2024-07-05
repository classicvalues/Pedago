from .user import TeacherManager  # Importing main implementations from user.py

class TeacherManagerWrapper:
    def __init__(self):
        self.teacher_manager = TeacherManager()

    def addTeacher(self, teacher_id: str, name: str, email: str) -> bool:
        return self.teacher_manager.addTeacher(teacher_id, name, email)

    def removeTeacher(self, teacher_id: str) -> bool:
        return self.teacher_manager.removeTeacher(teacher_id)

    def getTeacher(self, teacher_id: str) -> dict:
        return self.teacher_manager.getTeacher(teacher_id)

    def listTeachers(self) -> List[dict]:
        return self.teacher_manager.listTeachers()

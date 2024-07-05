from .user import User
from .student_manager import StudentManager
from .teacher_manager import TeacherManager
from typing import List

class UserManager:
    def __init__(self):
        self.users = {}
        self.student_manager = StudentManager()
        self.teacher_manager = TeacherManager()

    def addUser(self, user_id: str, user: User) -> bool:
        """Adds a new user to the system."""
        if user_id not in self.users:
            self.users[user_id] = user
            if isinstance(user, Student):
                self.student_manager.addStudent(user_id, user)
            elif isinstance(user, Instructor):
                self.teacher_manager.addTeacher(user_id, user)
            return True
        return False

    def updateUserDetails(self, user_id: str, name: str = None, email: str = None) -> bool:
        """Updates user details."""
        if user_id in self.users:
            user = self.users[user_id]
            if name:
                user.updateName(name)
            if email:
                user.updateEmail(email)
            return True
        return False

    def getUser(self, user_id: str) -> User:
        """Retrieves a user by their ID."""
        return self.users.get(user_id, None)

    def listUsers(self) -> List[User]:
        """Lists all users."""
        return list(self.users.values())

# pedago/user_manager.py

from .user import User

class UserManager:
    def __init__(self):
        self.users = {}

    def addUser(self, user_id: str, name: str, email: str, password: str, role: str) -> bool:
        """Adds a new user."""
        if user_id not in self.users:
            self.users[user_id] = User(user_id, name, email, password, role)
            return True
        return False

    def removeUser(self, user_id: str) -> bool:
        """Removes a user."""
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False

    def updateUserDetails(self, user_id: str, name: str = None, email: str = None, password: str = None) -> bool:
        """Updates user details."""
        if user_id in self.users:
            user = self.users[user_id]
            if name:
                user.name = name
            if email:
                user.email = email
            if password:
                user.password = password
            return True
        return False

    def authenticateUser(self, email: str, password: str) -> bool:
        """Authenticates user credentials."""
        for user in self.users.values():
            if user.email == email and user.password == password:
                return True
        return False

    def generateUserReport(self, user_id: str) -> dict:
        """Generates a report for a user."""
        if user_id in self.users:
            user = self.users[user_id]
            return {
                "user_id": user.user_id,
                "name": user.name,
                "email": user.email,
                "role": user.role
            }
        return {}

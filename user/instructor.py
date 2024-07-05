# pedago/user/instructor.py

from .user import User

class Instructor(User):
    def __init__(self, user_id: str, name: str, email: str, password: str, bio: str):
        super().__init__(user_id, name, email, password, role="instructor")
        self.bio = bio
        self.created_courses = []

    def addCourse(self, course_id: str):
        """Adds a course created by the instructor."""
        if course_id not in self.created_courses:
            self.created_courses.append(course_id)

    def removeCourse(self, course_id: str):
        """Removes a course created by the instructor."""
        if course_id in self.created_courses:
            self.created_courses.remove(course_id)

    def updateBio(self, bio: str):
        """Updates instructor's bio."""
        self.bio = bio

class User:
    def __init__(self, user_id: str, name: str, email: str, password: str, role: str):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.role = role
        self.enrolled_courses = []
        self.created_courses = []

    def updateProfile(self, name: str = None, email: str = None, password: str = None):
        """Updates user profile."""
        if name:
            self.name = name
        if email:
            self.email = email
        if password:
            self.password = password

    def enrollInCourse(self, course_id: str):
        """Enrolls user in a course."""
        self.enrolled_courses.append(course_id)

    def unenrollFromCourse(self, course_id: str):
        """Unenrolls user from a course."""
        if course_id in self.enrolled_courses:
            self.enrolled_courses.remove(course_id)

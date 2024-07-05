class Course:
    def __init__(self, course_id: str, instructor_id: str, title: str, description: str):
        self.course_id = course_id
        self.instructor_id = instructor_id
        self.title = title
        self.description = description
        self.syllabus = ""
        self.enrolled_students = []
        self.status = "draft"  # Possible values: "draft", "published", "archived"

    def updateTitle(self, title: str):
        """Updates course title."""
        self.title = title

    def updateDescription(self, description: str):
        """Updates course description."""
        self.description = description

    def addContent(self, content: str):
        """Adds content to course syllabus."""
        self.syllabus += content

    def publishCourse(self):
        """Publishes the course."""
        self.status = "published"

    def archiveCourse(self):
        """Archives the course."""
        self.status = "archived"

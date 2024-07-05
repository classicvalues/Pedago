# pedago/course/course.py

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
        """Adds content to the course."""
        self.syllabus += "\n" + content

    def removeContent(self, content: str):
        """Removes content from the course."""
        self.syllabus.replace(content, "")

    def updateStatus(self, status: str):
        """Updates course status."""
        self.status = status

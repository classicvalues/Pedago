# pedago/course/course_manager_wrapper.py

from datetime import datetime
from .course import CourseManager  # Importing main implementation from course.py

class CourseManagerWrapper:
    def __init__(self):
        self.course_manager = CourseManager()

    def createCourse(self, title: str, description: str, start_date: datetime, end_date: datetime, teacher_id: str) -> str:
        return self.course_manager.createCourse(title, description, start_date, end_date, teacher_id)

    def updateCourse(self, course_id: str, title: str = None, description: str = None, start_date: datetime = None, end_date: datetime = None, teacher_id: str = None) -> bool:
        return self.course_manager.updateCourseDetails(course_id, title, description)

    def getCourse(self, course_id: str) -> dict:
        course = self.course_manager.getCourse(course_id)
        if course:
            return {
                "course_id": course.course_id,
                "title": course.title,
                "description": course.description,
                "syllabus": course.syllabus,
                "status": course.status,
                "enrolled_students": course.enrolled_students
            }
        return {}

    def deleteCourse(self, course_id: str) -> bool:
        return self.course_manager.removeCourse(course_id)

    def enrollStudent(self, course_id: str, student_id: str) -> bool:
        return self.course_manager.enrollStudent(course_id, student_id)

    def removeStudent(self, course_id: str, student_id: str) -> bool:
        return self.course_manager.removeStudent(course_id, student_id)

    def listCourses(self, teacher_id: str = None) -> list:
        courses = self.course_manager.listCourses(teacher_id)
        return [{
            "course_id": course.course_id,
            "title": course.title,
            "description": course.description,
            "syllabus": course.syllabus,
            "status": course.status,
            "enrolled_students": course.enrolled_students
        } for course in courses]

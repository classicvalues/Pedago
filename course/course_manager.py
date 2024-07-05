# pedago/course/course_manager.py

from datetime import datetime
from typing import List
from .course import Course

class CourseManager:
    def __init__(self):
        self.courses = {}

    def createCourse(self, title: str, description: str, start_date: datetime, end_date: datetime, teacher_id: str) -> str:
        """Creates a new course and returns the course ID."""
        course_id = str(len(self.courses) + 1)  # Generate unique course ID
        course = Course(course_id, teacher_id, title, description)
        self.courses[course_id] = course
        return course_id

    def updateCourseDetails(self, course_id: str, title: str = None, description: str = None) -> bool:
        """Updates course details."""
        if course_id in self.courses:
            course = self.courses[course_id]
            if title:
                course.title = title
            if description:
                course.description = description
            return True
        return False

    def getCourse(self, course_id: str) -> Course:
        """Retrieves course details."""
        return self.courses.get(course_id, None)

    def removeCourse(self, course_id: str) -> bool:
        """Removes a course."""
        if course_id in self.courses:
            del self.courses[course_id]
            return True
        return False

    def enrollStudent(self, course_id: str, student_id: str) -> bool:
        """Enrolls a student in a course."""
        if course_id in self.courses:
            self.courses[course_id].enrolled_students.append(student_id)
            return True
        return False

    def removeStudent(self, course_id: str, student_id: str) -> bool:
        """Removes a student from a course."""
        if course_id in self.courses:
            if student_id in self.courses[course_id].enrolled_students:
                self.courses[course_id].enrolled_students.remove(student_id)
                return True
        return False

    def listCourses(self, teacher_id: str = None) -> List[Course]:
        """Lists all courses or courses by a specific teacher."""
        if teacher_id:
            return [course for course in self.courses.values() if course.instructor_id == teacher_id]
        return list(self.courses.values())

class AssessmentManager:
    def __init__(self):
        self.assessments = {}

    def createAssessment(self, course_id: str, assessment_id: str, assessment_type: str, details: dict):
        """Creates an assessment for a course."""
        if course_id not in self.assessments:
            self.assessments[course_id] = {}
        self.assessments[course_id][assessment_id] = {
            "assessment_type": assessment_type,
            "details": details
        }

    def updateAssessment(self, course_id: str, assessment_id: str, details: dict):
        """Updates an assessment for a course."""
        if course_id in self.assessments and assessment_id in self.assessments[course_id]:
            self.assessments[course_id][assessment_id]["details"] = details

    def gradeAssessment(self, course_id: str, assessment_id: str, student_id: str, grade: float):
        """Grades an assessment for a student in a course."""
        if course_id in self.assessments and assessment_id in self.assessments[course_id]:
            if "grades" not in self.assessments[course_id][assessment_id]:
                self.assessments[course_id][assessment_id]["grades"] = {}
            self.assessments[course_id][assessment_id]["grades"][student_id] = grade

    def generateAssessmentReport(self, course_id: str, assessment_id: str):
        """Generates an assessment report for a course."""
        if course_id in self.assessments and assessment_id in self.assessments[course_id]:
            return {
                "course_id": course_id,
                "assessment_id": assessment_id,
                "details": self.assessments[course_id][assessment_id]["details"],
                "grades": self.assessments[course_id][assessment_id].get("grades", {})
            }
        return {}

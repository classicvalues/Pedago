from typing import Optional
from .assessment import AssessmentManager  # Importing main implementation from assessment.py

class AssessmentManagerWrapper:
    def __init__(self):
        self.assessment_manager = AssessmentManager()

    def createAssessment(self, course_id: str, assessment_type: str, details: dict) -> str:
        return self.assessment_manager.createAssessment(course_id, assessment_type, details)

    def updateAssessment(self, assessment_id: str, details: dict) -> bool:
        return self.assessment_manager.updateAssessment(assessment_id, details)

    def gradeAssessment(self, assessment_id: str, student_id: str, grade: float) -> bool:
        return self.assessment_manager.gradeAssessment(assessment_id, student_id, grade)

    def generateAssessmentReport(self, assessment_id: str) -> Optional[dict]:
        return self.assessment_manager.generateAssessmentReport(assessment_id)

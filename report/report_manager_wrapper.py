from .report import ReportManager  # Importing main implementation from report.py

class ReportManagerWrapper:
    def __init__(self):
        self.report_manager = ReportManager()

    def generateUserActivityReport(self):
        return self.report_manager.generateUserActivityReport()

    def generateCoursePerformanceReport(self):
        return self.report_manager.generateCoursePerformanceReport()

    def generateFinancialReport(self):
        return self.report_manager.generateFinancialReport()

    def generateEnrollmentReport(self):
        return self.report_manager.generateEnrollmentReport()

"""
Hermes Feature Schema

This file defines the exact feature order expected by the trained model.
The order must always match the order used during model training.
"""

FEATURE_ORDER = [
    "Student Age",
    "Sex",
    "Graduated high-school type",
    "Scholarship type",
    "Additional work",
    "Regular artistic or sports activity",
    "Do you have a partner",
    "Total salary if available",
    "Transportation to the university",
    "Accomodation type in Cyprus",
    "Mother's education",
    "Father's education",
    "Number of sisters/brothers (if available)",
    "Parental status",
    "Mother's occupation",
    "Father's occupation",
    "Weekly study hours",
    "Reading frequency (non-scientific books/journals)",
    "Reading frequency (scientific books/journals)",
    "Attendance to the seminars/conferences related to the department",
    "Impact of your projects/activities on your success",
    "Attendance to classes",
    "Preparation to midterm exams 1",
    "Preparation to midterm exams 2",
    "Taking notes in classes",
    "Listening in classes",
    "Discussion improves my interest and success in the course",
    "Flip-classroom",
    "Cumulative grade point average in the last semester (/4.00)",
    "Expected Cumulative grade point average in the graduation (/4.00)",
    "Course ID"
]

TARGET_COLUMN = "GRADE"
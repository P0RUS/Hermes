import logging
import pandas as pd

from flask import Flask, render_template, request

from config import MODEL_PATH, DEBUG

from hermes.forms import build_student_dataframe
from hermes.prediction import HermesPredictor
app = Flask(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

hermes = HermesPredictor(MODEL_PATH)
logging.info("Hermes model loaded successfully.")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    form_data = {

        # 👤 Student Profile
        "Student Age": int(request.form["student_age"]),
        "Sex": int(request.form["sex"]),
        "Graduated high-school type": int(request.form["high_school_type"]),
        "Scholarship type": int(request.form["scholarship_type"]),

        # 🏠 Personal Background
        "Additional work": int(request.form["additional_work"]),
        "Regular artistic or sports activity": int(request.form["sports_activity"]),
        "Do you have a partner": int(request.form["partner"]),
        "Total salary if available": int(request.form["salary"]),
        "Transportation to the university": int(request.form["transportation"]),
        "Accomodation type in Cyprus": int(request.form["accommodation"]),

        # 👨‍👩‍👧 Family
        "Mother's education": int(request.form["mother_education"]),
        "Father's education": int(request.form["father_education"]),
        "Number of sisters/brothers (if available)": int(request.form["siblings"]),
        "Parental status": int(request.form["parental_status"]),
        "Mother's occupation": int(request.form["mother_occupation"]),
        "Father's occupation": int(request.form["father_occupation"]),

        # 📚 Study Habits
        "Weekly study hours": int(request.form["weekly_study_hours"]),
        "Reading frequency (non-scientific books/journals)": int(request.form["reading_frequency"]),
        "Reading frequency (scientific books/journals)": int(request.form["scientific_reading"]),
        "Attendance to the seminars/conferences related to the department": int(request.form["seminar_attendance"]),
        "Impact of your projects/activities on your success": int(request.form["project_impact"]),
        "Attendance to classes": int(request.form["class_attendance"]),
        "Preparation to midterm exams 1": int(request.form["midterm_preparation_1"]),
        "Preparation to midterm exams 2": int(request.form["midterm_preparation_2"]),
        "Taking notes in classes": int(request.form["taking_notes"]),
        "Listening in classes": int(request.form["listening"]),
        "Discussion improves my interest and success in the course": int(request.form["discussion"]),
        "Flip-classroom": int(request.form["flip_classroom"]),

        # 🎓 Academic History
        "Cumulative grade point average in the last semester (/4.00)": float(request.form["previous_gpa"]),
        "Expected Cumulative grade point average in the graduation (/4.00)": float(request.form["expected_gpa"]),
        "Course ID": int(request.form["course_id"])
    }

    try:

        student = build_student_dataframe(form_data)

        prediction = hermes.predict(student)

        logging.info(f"Prediction generated: Grade {prediction[0]}")

        return render_template(
            "result.html",
            prediction=prediction[0]
        )

    except Exception as e:

        logging.exception("Prediction failed.")

        return render_template(
            "error.html",
            error=str(e)
        ), 500

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template("500.html"), 500

if __name__ == "__main__":
    logging.info("Starting Hermes...")
    app.run(debug=DEBUG)
import pandas as pd

from hermes.schema import FEATURE_ORDER


def build_student_dataframe(form_data):

    student = pd.DataFrame([form_data])

    return student[FEATURE_ORDER]
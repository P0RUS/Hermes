import joblib


class HermesPredictor:
    """
    Loads a trained Hermes model and performs predictions.
    """

    def __init__(self, model_path):
        self.model = joblib.load(model_path)

    def predict(self, student):
        """
        Predict the grade for one or more students.

        Parameters
        ----------
        student : pandas.DataFrame
            Student feature data.

        Returns
        -------
        numpy.ndarray
            Predicted grade(s).
        """
        return self.model.predict(student)
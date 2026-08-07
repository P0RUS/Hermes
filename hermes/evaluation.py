import numpy as np

from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_absolute_error


def evaluate_model(
    model,
    X_train,
    X_test,
    y_train,
    y_test,
    model_name=None
):

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    mae = mean_absolute_error(y_test, predictions)

    grade_difference = np.abs(y_test - predictions)

    within_one = np.mean(grade_difference <= 1)

    name = model_name or model.__class__.__name__

    return {
        "Model": name,
        "Accuracy": accuracy,
        "MAE": mae,
        "Within ±1": within_one
    }
import numpy as np

from sklearn.metrics import accuracy_score

def evaluate_model(model, X_train, X_test, y_train, y_test):

    # Train
    model.fit(X_train, y_train)

    # Predict
    predictions = model.predict(X_test)

    # Metrics
    accuracy = accuracy_score(y_test, predictions)

    mae = np.mean(np.abs(y_test - predictions))

    within_one = np.mean(np.abs(y_test - predictions) <= 1)

    return {
        "Model": model.__class__.__name__,
        "Accuracy": accuracy,
        "MAE": mae,
        "Within ±1": within_one
    }
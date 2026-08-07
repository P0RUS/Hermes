import json
import joblib


def save_model(model, path):
    """
    Save a trained machine learning model.
    """
    joblib.dump(model, path)


def load_model(path):
    """
    Load a trained machine learning model.
    """
    return joblib.load(path)


def save_json(data, path):
    """
    Save a dictionary as a JSON file.
    """
    with open(path, "w") as file:
        json.dump(data, file, indent=4)


def load_json(path):
    """
    Load data from a JSON file.
    """
    with open(path, "w", encoding="utf-8") as file:
        return json.load(file)
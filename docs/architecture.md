# 🏛️ Hermes Architecture

```text
                         🪽 Hermes

                   Student Input (Browser)
                             │
                             ▼
                    HTML / CSS Interface
                             │
                             ▼
                      Flask Application
                           (app.py)
                             │
                             ▼
                   Form Processing Module
                        (forms.py)
                             │
                             ▼
                 Feature Schema Validation
                        (schema.py)
                             │
                             ▼
                   HermesPredictor Class
                     (prediction.py)
                             │
                             ▼
               Random Forest Model (.pkl)
                             │
                             ▼
                  Predicted Student Grade
```

## Module Responsibilities

### app.py
- Handles HTTP requests
- Receives form input
- Returns rendered HTML pages

### forms.py
- Converts submitted form data into a DataFrame
- Ensures compatibility with the trained model

### schema.py
- Defines the required feature order
- Keeps training and prediction consistent

### prediction.py
- Loads the trained model
- Generates predictions

### models.py
- Defines machine learning model configurations

### evaluation.py
- Evaluates model performance
- Computes Accuracy, MAE, and Within ±1 metrics

### visualization.py
- Generates evaluation charts
- Displays feature importance and comparison plots

### utils.py
- General helper functions
- Model and JSON persistence

### config.py
- Central application configuration
- Model path
- Version
- Debug mode
```
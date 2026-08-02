# Hermes 🪽

> 🚧 **Hermes v0.1 — Research Phase**

Hermes is a machine-learning project exploring the factors associated with student academic performance.

The project uses student data to investigate relationships between academic habits and outcomes, with the long-term goal of building an interactive system that can provide data-driven performance insights.

## Why Hermes?

In Greek mythology, Hermes is the messenger of the gods.

This project follows a similar idea: taking raw information, finding meaningful patterns within it, and communicating those insights in a useful way.

## Current Progress

- [x] Project environment setup
- [x] Dataset acquisition
- [x] Initial data inspection
- [x] Missing-value and duplicate checks
- [x] Exploratory data analysis
- [x] Feature correlation analysis
- [ ] Baseline machine-learning model
- [ ] Model comparison and evaluation
- [ ] Prediction system
- [ ] Web interface

## Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- scikit-learn
- Jupyter Notebook

## Project Structure

    Hermes/
    ├── data/
    ├── model/
    ├── notebooks/
    │   └── analysis.ipynb
    ├── app.py
    ├── requirements.txt
    └── README.md

## Status

🚧 Currently under development.

## 📊 Model Evaluation

Hermes does not select models based solely on classification accuracy. Since the target variable represents ordered grade categories, each model is evaluated using multiple complementary metrics:

- Accuracy
- Mean Absolute Error (MAE)
- Predictions within ±1 grade category

This evaluation strategy provides a more meaningful assessment of prediction quality and allows fairer comparison between machine learning models.

## 🚀 Project Progress

- [x] Project environment setup
- [x] Dataset acquisition
- [x] Initial data inspection
- [x] Missing-value and duplicate checks
- [x] Exploratory data analysis (EDA)
- [x] Feature correlation analysis
- [x] Logistic Regression baseline
- [x] Decision Tree benchmark
- [x] Random Forest benchmark
- [x] K-Nearest Neighbors (KNN) benchmark
- [ ] Cross-validation
- [ ] Feature importance analysis
- [ ] Hyperparameter tuning
- [ ] Model comparison report
- [ ] Prediction system
- [ ] Flask web application
- [ ] Interactive dashboard
- [ ] Model deployment

## 🗺️ Roadmap

### Hermes v0.1
- Initial data exploration
- Baseline machine learning models
- Model benchmarking
- Evaluation metrics

### Hermes v0.2
- Cross-validation
- Feature importance analysis
- Hyperparameter tuning
- Improved documentation

### Hermes v0.3
- Prediction pipeline
- Flask web application
- Interactive dashboard

### Hermes v1.0
- Stable web application
- Live deployment
- Polished documentation
- Portfolio-ready release
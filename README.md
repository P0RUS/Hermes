# 🪽 Hermes

> **Hermes v1.0 – The Herald**

**Knowledge enters. Insight leaves.**

Hermes is an end-to-end machine learning web application that predicts student academic performance using supervised learning techniques. Built with Python, scikit-learn, and Flask, the project demonstrates the complete machine learning workflow—from data exploration and model evaluation to deployment through an interactive web interface.

Hermes was developed as an evidence-driven machine learning project. Every major improvement is supported by experiments, cross-validation, and documented engineering decisions rather than relying on a single evaluation metric.

---

# ✨ Features

- 📊 Exploratory Data Analysis (EDA)
- 🤖 Multiple machine learning models
  - Logistic Regression
  - Decision Tree
  - Random Forest
  - K-Nearest Neighbors
- 📈 Cross-validation
- 🌲 Feature importance analysis
- ⚙️ Hyperparameter tuning
- 💾 Model persistence with Joblib
- 🌐 Flask web application
- 🖥️ Interactive prediction interface
- 📁 Modular Python package architecture
- 📜 Logging and error handling

---

# 🏛️ Why Hermes?

In Greek mythology, Hermes is the messenger of the gods.

This project follows the same philosophy: transforming raw educational data into meaningful insights and presenting those insights through a clean and accessible interface.

Rather than simply predicting grades, Hermes aims to demonstrate the complete lifecycle of a machine learning application.

---

# 📊 Evaluation Strategy

Hermes evaluates models using multiple complementary metrics:

- Accuracy
- Mean Absolute Error (MAE)
- Predictions Within ±1 Grade
- Cross-Validation

Using several evaluation metrics provides a more reliable assessment than relying on classification accuracy alone, especially for ordered grade categories.

---

# 🛠️ Tech Stack

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Joblib
- Jupyter Notebook

---

# 📂 Project Structure

```text
Hermes/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── CHANGELOG.md
├── ROADMAP.md
│
├── data/
├── docs/
├── experiments/
├── hermes/
│   ├── evaluation.py
│   ├── forms.py
│   ├── models.py
│   ├── prediction.py
│   ├── schema.py
│   ├── utils.py
│   └── visualization.py
│
├── model/
├── notebooks/
├── static/
└── templates/
```
## 🏗️ Architecture

The Hermes architecture is documented in:

```text
docs/architecture.md
---

# 🚀 Running Hermes

Clone the repository

```bash
git clone <repository-url>
cd Hermes
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

---

# 📸 Application

> Screenshots of the home page, prediction page, and result page will be added here.

---

# 📈 Current Status

✅ Machine learning pipeline complete

✅ Model evaluation complete

✅ Flask application complete

✅ Interactive prediction system complete

🚧 Portfolio polish and documentation improvements ongoing

---

# 🎯 Future Improvements

- Better input validation
- Improved UI/UX
- Additional visualizations
- Deployment to the cloud

---

# 📜 License

This project is released under the MIT License.
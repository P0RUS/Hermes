import matplotlib.pyplot as plt


def plot_model_comparison(benchmark):

    benchmark.plot(
        x="Model",
        y="Accuracy",
        kind="bar",
        legend=False
    )

    plt.title("Model Accuracy Comparison")
    plt.ylabel("Accuracy")
    plt.tight_layout()
    plt.show()

def plot_feature_importance(feature_importance):

    top_features = feature_importance.head(10)

    plt.figure(figsize=(10,6))

    top_features.sort_values("Importance").plot(
        kind="barh",
        x="Feature",
        y="Importance",
        legend=False
    )

    plt.title("Top 10 Feature Importance")

    plt.tight_layout()

    plt.show()

def plot_cross_validation(scores):

    plt.figure(figsize=(8,5))

    plt.plot(
        range(1, len(scores)+1),
        scores,
        marker="o"
    )

    plt.title("Cross Validation Scores")

    plt.xlabel("Fold")

    plt.ylabel("Accuracy")

    plt.grid(True)

    plt.show()

def plot_experiment_results():
    """
    Placeholder for future experiment visualizations.

    Planned Use:
    - Experiment 001: Compare Random Forest performance with and without Course ID.
    - Experiment 002: Compare default vs. tuned Random Forest.
    - Future experiments: Automatically generate comparison charts for reports.
    """
    raise NotImplementedError(
        "Experiment visualization will be implemented in a future Hermes release."
    )
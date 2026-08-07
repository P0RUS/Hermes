from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier


def logistic_regression():
    return LogisticRegression(max_iter=5000)


def decision_tree():
    return DecisionTreeClassifier(random_state=42)


def random_forest():
    return RandomForestClassifier(
        n_estimators=50,
        max_depth=10,
        min_samples_split=2,
        min_samples_leaf=1,
        random_state=42
    )


def create_knn():
    return KNeighborsClassifier()
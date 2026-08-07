# 🧪 Experiment 002 — The Balanced Forest

**Version:** Hermes v0.4 – The Forge

---

## Question

Can the performance of the Random Forest model be improved through hyperparameter tuning?

---

## Background

The default Random Forest model achieved the strongest performance during benchmarking and cross-validation.

This experiment investigates whether adjusting the model's hyperparameters can further improve predictive performance while maintaining good generalization.

---

## Hypothesis

Optimizing the Random Forest hyperparameters will improve cross-validation accuracy without introducing unnecessary model complexity.

---

## Method

- Model: Random Forest Classifier
- Evaluation Strategy: 5-Fold Cross Validation
- Scoring Metric: Accuracy
- Optimization Method: GridSearchCV

### Parameter Grid

| Parameter | Values Tested |
|-----------|---------------|
| n_estimators | 50, 100, 200 |
| max_depth | None, 5, 10 |
| min_samples_split | 2, 5 |
| min_samples_leaf | 1, 2 |

---

## Results

### Best Parameters

```python
{
    "max_depth": 10,
    "min_samples_leaf": 1,
    "min_samples_split": 2,
    "n_estimators": 50
}
```

### Best Cross-Validation Accuracy

**33.10%**

---

## Observations

- A maximum tree depth of **10** outperformed unrestricted tree growth.
- Increasing the number of trees beyond **50** did not improve performance for this dataset.
- The default values for `min_samples_split` and `min_samples_leaf` remained optimal.
- Hyperparameter tuning improved the Random Forest's cross-validation accuracy compared to the default configuration.

---

## Conclusion

Hyperparameter tuning increased the model's cross-validation accuracy from **30.34%** to **33.10%**, making the tuned Random Forest the strongest model evaluated in Hermes so far.

The experiment also demonstrated that improved performance does not necessarily require a more complex model. Instead, selecting appropriate hyperparameters produced better generalization while keeping the model relatively efficient.

---

## What We Learned

- Model performance depends on both the algorithm and its configuration.
- More trees do not always produce better results.
- Limiting tree depth can improve generalization by reducing unnecessary complexity.
- Systematic hyperparameter tuning is a valuable step in building reliable machine-learning models.
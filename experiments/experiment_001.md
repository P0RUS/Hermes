# 🧪 Experiment 001 — The Hidden Variable

**Version:** Hermes v0.3 – The Oracle

---

## Question

Does including **Course ID** improve the Random Forest model's predictive performance, or does it introduce unnecessary dataset-specific information?

---

## Background

The original dataset includes **Course ID** as one of the input features. While this information may correlate with student grades, it does not describe the student's own characteristics or study habits.

This experiment investigates whether removing Course ID improves the model's ability to generalize by relying only on student-related information.

---

## Hypothesis

Removing **Course ID** will reduce reliance on course-specific information while maintaining comparable predictive performance.

---

## Method

- Model: Random Forest Classifier
- Evaluation Strategy: Train/Test Split (80/20)
- Scoring Metric: Accuracy
- Comparison:
  - Random Forest with Course ID
  - Random Forest without Course ID

---

## Results

### Accuracy Comparison

| Configuration | Accuracy |
|--------------|---------:|
| With Course ID | **36.67%** |
| Without Course ID | **31.67%** |

---

## Observations

- Removing **Course ID** reduced overall prediction accuracy.
- The model benefited from the additional information provided by the course identifier.
- Course ID appears to capture meaningful differences between courses that influence grade prediction.
- The experiment demonstrated the importance of validating assumptions through controlled testing.

---

## Conclusion

Removing Course ID decreased predictive performance by approximately **5 percentage points**.

Although the initial expectation was that removing the feature might improve generalization, the results showed that **Course ID provides meaningful predictive information** for this dataset. Hermes therefore retains the feature in its final prediction pipeline.

---

## What We Learned

- Assumptions should always be tested experimentally.
- Features that appear unimportant may contain valuable predictive information.
- Controlled experiments provide stronger evidence than intuition.
- Feature selection should be based on measurable performance.
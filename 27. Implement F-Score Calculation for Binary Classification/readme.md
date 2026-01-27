# Implement F-Score Calculation for Binary Classification

## 1. Problem Explanation

The F-Score is a metric used in binary classification to measure a model’s accuracy by combining two important metrics: Precision and Recall. Precision tells us how many predicted positives were actually correct, while Recall tells us how many actual positives were correctly found by the model. The F-Score balances these two metrics into a single value, making it easier to judge model performance when dealing with imbalanced datasets.

In this task, we implement a function that calculates the F-Score given the true labels, predicted labels, and a beta value. The beta parameter controls the importance of Recall relative to Precision. When beta = 1, the formula becomes the F1-score, which gives equal importance to Precision and Recall.

---

## 2. Code with Comments

```python
import numpy as np

def f_score(y_true, y_pred, beta):
    # Count True Positives: cases where both true and predicted labels are 1
    tp = np.sum((y_true == 1) & (y_pred == 1))

    # Count False Negatives: true label is 1 but predicted label is 0
    fn = np.sum((y_true == 1) & (y_pred == 0))

    # Count False Positives: true label is 0 but predicted label is 1
    fp = np.sum((y_true == 0) & (y_pred == 1))

    # Calculate recall = TP / (TP + FN)
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0

    # Calculate precision = TP / (TP + FP)
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0

    # Multiply precision and recall for numerator
    op = precision * recall

    # Denominator of F-score formula
    div = ((beta**2) * precision) + recall

    # If denominator or numerator is zero, return 0 to avoid division error
    if div == 0 or op == 0:
        return 0.0

    # Apply F-score formula
    score = (1 + (beta ** 2)) * op / div

    # Round the final result to three decimal places
    return round(score, 3)
```

---

## 3. Approach and Logic Explained

### Step 1: Count TP, FP, and FN

We first compute:

* True Positives (TP): correct positive predictions
* False Positives (FP): incorrect positive predictions
* False Negatives (FN): missed positive cases

These values form the foundation for Precision and Recall.

### Step 2: Compute Precision and Recall

Precision is calculated as:

TP / (TP + FP)

Recall is calculated as:

TP / (TP + FN)

We add safety checks to avoid division by zero.

### Step 3: Compute F-Score

The general F-score formula is:

(1 + beta²) * (precision * recall) / (beta² * precision + recall)

The beta parameter adjusts the importance of recall compared to precision.

* beta = 1 gives equal importance (F1-score)
* beta > 1 favors recall
* beta < 1 favors precision

### Step 4: Final Output

The result is rounded to three decimal places, as required.

---

## 4. Why This Method Works

This solution directly follows the mathematical definition of the F-score. It first computes precision and recall using logical conditions on NumPy arrays, making the implementation fast and clean. The formula then combines them into a single balanced metric.
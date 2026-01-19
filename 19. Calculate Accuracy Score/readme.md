# Calculate Accuracy Score

## 1. Problem Overview

In machine learning, evaluating how well a model performs is just as important as building the model itself. One of the most basic and widely used evaluation metrics is **accuracy**.

The **Calculate Accuracy Score** problem focuses on computing the accuracy of a model by comparing its predicted labels with the true (actual) labels.

**Accuracy** is defined as:

> The ratio of correctly predicted samples to the total number of samples.

This problem asks us to implement our own accuracy calculation function using NumPy, without relying on external libraries like scikit-learn.

---

## 2. What Is the Accuracy Score?

Given two arrays:

* `y_true`: the ground-truth (actual) labels
* `y_pred`: the labels predicted by the model

The accuracy score tells us **how many predictions were correct overall**.

Mathematically:

```
accuracy = (number of correct predictions) / (total number of predictions)
```

Accuracy values range between **0 and 1**, where:

* `1.0` means all predictions are correct
* `0.0` means all predictions are incorrect

---

## 3. Solution Code With Comments
```python
import numpy as np

def accuracy_score(y_true, y_pred):
    # Compare true labels with predicted labels
    # This creates a boolean array: True where labels match, False otherwise
    correct_predictions = (y_true == y_pred)

    # Count how many predictions are correct
    # True is treated as 1 and False as 0 in NumPy
    correct_count = np.sum(correct_predictions, axis=0)

    # Divide the number of correct predictions by total samples
    accuracy = correct_count / len(y_true)

    return accuracy
```

---

## 4. Step-by-Step Approach and Logic

1. **Compare predictions with true labels**
   Using `y_true == y_pred`, we compare each element. NumPy performs this comparison element-wise.

2. **Convert matches into counts**
   The comparison results in a boolean array. When passed to `np.sum`, `True` values count as `1` and `False` values count as `0`.

3. **Normalize by total samples**
   Dividing by `len(y_true)` converts the count into a ratio between 0 and 1.

4. **Return the accuracy score**
   The final value represents the proportion of correct predictions.

---

## 5. Example Walkthrough

### Input

```python
y_true = np.array([1, 0, 1, 1, 0, 1])
y_pred = np.array([1, 0, 0, 1, 0, 1])
```

### Comparison Result

```
[True, True, False, True, True, True]
```

* Correct predictions: 5
* Total predictions: 6

### Accuracy Calculation

```
accuracy = 5 / 6 = 0.8333333333333334
```

---

## 6. Alternative Ways to Compute Accuracy

### Method 1: Using NumPy Mean (Simpler)

```python
accuracy = np.mean(y_true == y_pred)
```

**Why this works:**

* `True` becomes `1`, `False` becomes `0`
* Taking the mean automatically gives the accuracy

### Comparison of Approaches

| Approach                 | Explanation                    | Beginner Friendly               |
| ------------------------ | ------------------------------ | ------------------------------- |
| `np.sum(...) / len(...)` | Explicit counting and division | Very clear and educational      |
| `np.mean(...)`           | Short and concise              | Easier once NumPy is understood |

Both approaches give the **same result**. The provided solution is better for learning because it shows each step clearly.

---

## 7. Time and Space Complexity

* **Time Complexity:** `O(n)`
  Each element is compared once.

* **Space Complexity:** `O(1)`
  Only a small number of extra variables are used.

---

## 8. Key Takeaways

* Accuracy is the simplest evaluation metric in machine learning.
* It works best for **balanced datasets**.
* NumPy allows fast and clean element-wise comparisons.
* Writing your own metrics helps you understand how ML libraries work internally.
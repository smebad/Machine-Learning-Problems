# Implement Precision Metric

## 1. Problem Overview

In machine learning classification tasks, we often want to evaluate how good a model’s predictions are. One important evaluation metric is **precision**. Precision tells us how many of the samples that the model predicted as positive are actually positive.

The goal of this problem is to implement a function that calculates the precision score given two arrays:

* `y_true`: the actual labels
* `y_pred`: the predicted labels from the model

Both arrays contain binary values (0 or 1), where 1 usually represents the positive class and 0 represents the negative class.

---

## 2. What is Precision?

Precision is defined as:

Precision = True Positives / (True Positives + False Positives)

Where:

* **True Positives (TP)** are cases where the model predicted 1 and the true label is also 1
* **False Positives (FP)** are cases where the model predicted 1 but the true label is 0

Precision answers the question:

"When the model predicts positive, how often is it correct?"

---

## 3. Code Explanation With Comments

Below is your provided solution with added comments to make each step clear.

```python
import numpy as np

def precision(y_true, y_pred):
    # Count how many times both y_true and y_pred are 1
    # These are the True Positives (TP)
    true_positives = np.sum((y_true == 1) & (y_pred == 1))

    # Count how many times y_true is 0 but y_pred is 1
    # These are the False Positives (FP)
    false_positives = np.sum((y_true == 0) & (y_pred == 1))

    # If TP + FP is greater than 0, calculate precision
    # Otherwise, return 0.0 to avoid division by zero
    return true_positives / (true_positives + false_positives) if (true_positives + false_positives) > 0 else 0.0
```

---

## 4. Step-by-Step Logic

1. **Compare true and predicted labels**
   We use NumPy conditions to find where predictions match the true labels.

2. **Find True Positives**
   These are the cases where both `y_true` and `y_pred` are 1.

3. **Find False Positives**
   These are the cases where `y_pred` is 1 but `y_true` is 0.

4. **Apply the precision formula**
   We divide the number of true positives by the total number of predicted positives (TP + FP).

5. **Handle edge cases**
   If there are no predicted positives, the function returns 0.0 to avoid dividing by zero.

---

## 5. Test Case

```python
y_true = np.array([1, 0, 1, 1, 0, 1])
y_pred = np.array([1, 0, 1, 0, 0, 1])

result = precision(y_true, y_pred)
print(result)
```

**Output:**

```
1.0
```

Explanation:

* True Positives = 3 (positions where both arrays have 1)
* False Positives = 0
* Precision = 3 / (3 + 0) = 1.0

---

## 6. Why Precision is Important

Precision is especially important when false positives are costly. For example:

* Spam detection: you do not want to mark a real email as spam
* Medical diagnosis: you do not want to say someone is sick when they are not

A high precision means that when the model predicts positive, it is usually correct.

---

## 7. Key Takeaways

* Precision measures the quality of positive predictions
* It focuses on how accurate the positive predictions are
* It is calculated using True Positives and False Positives
* NumPy makes it easy to compute these values using logical conditions
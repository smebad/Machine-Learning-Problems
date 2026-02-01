# Calculate Root Mean Square Error (RMSE)

## 1. What is RMSE and What Problem Does It Solve?

**Root Mean Square Error (RMSE)** is a commonly used evaluation metric in Machine Learning and statistics, especially for **regression problems**.

It measures how far the predicted values are from the actual (true) values on average.

In simple words:

* RMSE tells us **how wrong our predictions are**.
* The smaller the RMSE, the better the model is performing.

### Why Do We Need RMSE?

When building regression models (like predicting house prices, temperature, stock prices, etc.), we need a way to check:

* How close are the predictions to real values?

RMSE solves this by:

1. Calculating the error for each prediction.
2. Squaring those errors (to avoid negative values).
3. Taking the average.
4. Taking the square root to bring the value back to the original scale.

### Mathematical Formula

RMSE is defined as:

RMSE = sqrt( (1/n) * Σ (y_true - y_pred)² )

Where:

* `n` = number of data points
* `y_true` = actual values
* `y_pred` = predicted values

---

## 2. Code With Comments

```python
import numpy as np

# Function to calculate Root Mean Square Error
def rmse(y_true, y_pred):
    # Check if both arrays have the same shape
    # If not, comparison is invalid
    if y_true.shape != y_pred.shape:
        raise ValueError("Arrays must have the same shape")
    
    # Check if arrays are empty
    # RMSE cannot be computed without data
    if y_true.size == 0:
        raise ValueError("Arrays cannot be empty")
    
    # Step 1: Subtract predictions from actual values
    # Step 2: Square the differences
    # Step 3: Take the mean of squared differences
    # Step 4: Take the square root
    # Step 5: Round result to 3 decimal places
    return round(np.sqrt(np.mean((y_true - y_pred) ** 2)), 3)

# Test Case
y_true = np.array([3, -0.5, 2, 7])
y_pred = np.array([2.5, 0.0, 2, 8])

print(rmse(y_true, y_pred))  # Output: 0.612
```

---

## 3. Solution, Approach, and Logic

Let’s break down what happens step by step.

### Step 1: Find the Errors

We subtract predicted values from actual values:

```
[3 - 2.5, -0.5 - 0, 2 - 2, 7 - 8]
= [0.5, -0.5, 0, -1]
```

These are called **residuals (errors)**.

---

### Step 2: Square the Errors

We square each value to:

* Remove negative signs
* Penalize larger errors more

```
[0.25, 0.25, 0, 1]
```

---

### Step 3: Take the Mean

Find the average of squared errors:

```
(0.25 + 0.25 + 0 + 1) / 4 = 0.375
```

---

### Step 4: Take Square Root

```
sqrt(0.375) = 0.612
```

This brings the value back to the original unit.

---

### Step 5: Final RMSE

```
RMSE = 0.612
```

This means that on average, the model’s predictions are off by **about 0.612 units**.

---

## Handling Edge Cases

The function also handles important edge cases:

### 1. Mismatched Shapes

If arrays are not the same size:

```python
raise ValueError("Arrays must have the same shape")
```

This prevents comparing unrelated data.

---

### 2. Empty Arrays

If arrays have no values:

```python
raise ValueError("Arrays cannot be empty")
```

You cannot compute RMSE without data.

---

## Key Takeaways

* RMSE measures how far predictions are from actual values.
* Lower RMSE means better model performance.
* It is widely used in regression problems.
* Squaring emphasizes large errors.
* Square root brings result back to original scale.

In real projects, RMSE is one of the **first metrics used to judge a regression model**.

---

## When to Use RMSE

Use RMSE when:

* You are solving a regression problem.
* You want to heavily penalize large mistakes.
* Your target values are numerical and continuous.

Avoid RMSE when:

* You are doing classification.
* Your data contains extreme outliers (RMSE is sensitive to them).
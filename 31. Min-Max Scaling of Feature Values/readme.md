# Min-Max Scaling of Feature Values

## 1. What is Min-Max Scaling and What Problem Does It Solve?

**Min-Max Scaling (also called Min-Max Normalization)** is a data preprocessing technique used in Machine Learning to scale numerical features into a fixed range, usually between **0 and 1**.

In simple words:

* It rescales your data so that the smallest value becomes 0.
* The largest value becomes 1.
* All other values are placed proportionally in between.

### Why Do We Need Min-Max Scaling?

In real-world datasets, features often have very different ranges.

Example:

* Age: 0–100
* Salary: 10,000–1,000,000

If we use these directly in a model:

* The model will give more importance to salary just because the numbers are bigger.

Min-Max Scaling solves this problem by:

* Bringing all features to the same scale.
* Ensuring that each feature contributes fairly to the model.

This is especially important for algorithms like:

* Gradient Descent
* KNN (K-Nearest Neighbors)
* Neural Networks
* SVM

---

### Mathematical Formula

Min-Max Scaling is defined as:

Scaled Value = (x - min(x)) / (max(x) - min(x))

Where:

* `x` is the original value
* `min(x)` is the minimum value in the dataset
* `max(x)` is the maximum value in the dataset

---

## 2. Code With Comments

```python
# Function to apply Min-Max Scaling
def min_max(x: list[float]) -> list[float]:
    # Find the minimum value in the list
    x_min = min(x)
    
    # Find the maximum value in the list
    x_max = max(x)
    
    # Edge case: if all values are the same
    # Then max - min = 0, which would cause division by zero
    # In this case, return a list of 0.0
    if x_max == x_min:
        return [0.0] * len(x)
    
    # Apply Min-Max formula to each value
    # (val - x_min) / (x_max - x_min)
    return [(val - x_min) / (x_max - x_min) for val in x]

# Test Cases
print(min_max([1, 2, 3, 4, 5]))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
print(min_max([10, 20, 30]))    # Output: [0.0, 0.5, 1.0]
print(min_max([5, 5, 5]))       # Output: [0.0, 0.0, 0.0]
```

---

## 3. Solution, Approach, and Logic

Let’s understand the logic step by step using an example.

### Example Input

```
[1, 2, 3, 4, 5]
```

---

### Step 1: Find Min and Max

```
min = 1
max = 5
```

---

### Step 2: Apply Formula to Each Value

Formula:

```
(val - min) / (max - min)
```

For each value:

| Value | Calculation       | Result |
| ----- | ----------------- | ------ |
| 1     | (1 - 1) / (5 - 1) | 0.0    |
| 2     | (2 - 1) / 4       | 0.25   |
| 3     | (3 - 1) / 4       | 0.5    |
| 4     | (4 - 1) / 4       | 0.75   |
| 5     | (5 - 1) / 4       | 1.0    |

Final Output:

```
[0.0, 0.25, 0.5, 0.75, 1.0]
```

---

## Handling Edge Case: All Values Same

Example:

```
[5, 5, 5]
```

Here:

* min = 5
* max = 5

So:

```
max - min = 0
```

This would cause division by zero.

So the function returns:

```
[0.0, 0.0, 0.0]
```

This makes sense because:

* There is no variation in the data.
* All values are identical.

---

## Why This Solution Is Good

This implementation is:

* Simple
* Efficient
* Safe (handles edge case)
* Easy to read

It uses:

* Built-in `min()` and `max()`
* List comprehension for clean transformation

---

## Key Takeaways

* Min-Max Scaling rescales data between 0 and 1.
* It prevents large numbers from dominating small ones.
* It is essential for many ML algorithms.
* It preserves the original data distribution.
* It is sensitive to outliers.

---

## When to Use Min-Max Scaling

Use it when:

* Your features have different ranges.
* You are using distance-based models.
* You want faster convergence in training.

Avoid it when:

* Your data has extreme outliers.
* You need a scale that is robust to noise.

In those cases, consider **Standardization (Z-score scaling)** instead.
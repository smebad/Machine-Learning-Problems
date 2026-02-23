# Calculate Jaccard Index for Binary Classification

## 1. What is the Jaccard Index and What Problem Does It Solve?

The **Jaccard Index** is a metric used to measure the similarity between two sets. In Machine Learning, it is commonly used in **binary classification** to compare the similarity between:

* True labels (`y_true`)
* Predicted labels (`y_pred`)

It tells us how much overlap exists between the actual and predicted positive values.

---

### Why Do We Need the Jaccard Index?

In binary classification, we want to know:

* How accurately the model predicts positive cases.
* How much overlap exists between predicted positives and actual positives.

The Jaccard Index helps quantify this overlap.

It is especially useful in:

* Image segmentation
* Information retrieval
* Recommendation systems
* Medical diagnosis

---

### Mathematical Formula

The Jaccard Index is defined as:

Jaccard Index = Intersection / Union

Where:

* **Intersection** = Number of elements where both `y_true` and `y_pred` are 1
* **Union** = Number of elements where at least one of `y_true` or `y_pred` is 1

Range:

* 0 → No overlap
* 1 → Perfect overlap

---

## 2. Code With Comments

```python
import numpy as np

# Function to calculate Jaccard Index
def jaccard_index(y_true, y_pred):

    # Calculate intersection
    # Count positions where both true and predicted values are 1
    intersection = np.sum((y_true == 1) & (y_pred == 1))

    # Calculate union
    # Count positions where either true OR predicted value is 1
    union = np.sum((y_true == 1) | (y_pred == 1))

    # Calculate Jaccard Index
    result = intersection / union

    # Handle edge case where union = 0
    # This happens when both arrays contain only zeros
    if np.isnan(result):
        return 0.0

    # Round result to 3 decimal places
    return round(result, 3)

# Test Case
y_true = np.array([1, 0, 1, 1, 0, 1])
y_pred = np.array([1, 0, 1, 0, 0, 1])

print(jaccard_index(y_true, y_pred))  # Output: 0.75
```

---

## 3. Step-by-Step Example

Input:

```
y_true = [1, 0, 1, 1, 0, 1]
y_pred = [1, 0, 1, 0, 0, 1]
```

---

### Step 1: Find Intersection

Positions where both are 1:

```
Index:   0 1 2 3 4 5
y_true:  1 0 1 1 0 1
y_pred:  1 0 1 0 0 1
Match:   Y   Y     Y
```

Intersection count:

```
3
```

---

### Step 2: Find Union

Positions where at least one is 1:

```
Index:   0 1 2 3 4 5
Union:   Y   Y Y     Y
```

Union count:

```
4
```

---

### Step 3: Apply Formula

```
Jaccard Index = 3 / 4
              = 0.75
```

---

## 4. Logic and Approach Explained Simply

The logic follows these steps:

Step 1: Compare both arrays element by element

Step 2: Count intersection

```
(y_true == 1) AND (y_pred == 1)
```

Step 3: Count union

```
(y_true == 1) OR (y_pred == 1)
```

Step 4: Divide intersection by union

Step 5: Handle edge cases safely

---

## 5. Edge Cases Handling

### Case 1: No Overlap

Example:

```
y_true = [1,1,1]
y_pred = [0,0,0]
```

Intersection = 0
Union = 3

Result:

```
0.0
```

---

### Case 2: Both Arrays All Zeros

Example:

```
y_true = [0,0,0]
y_pred = [0,0,0]
```

Intersection = 0
Union = 0

This would cause division by zero.

Handled safely:

```
Return 0.0
```

---

## 6. When to Use Jaccard Index in Machine Learning

Use when:

* Evaluating binary classification
* Measuring similarity between sets
* Working with imbalanced datasets
* Image segmentation tasks

---

## 7. Jaccard Index vs Accuracy

Accuracy considers both positive and negative matches.

Jaccard focuses only on positive overlap.

This makes it more useful when:

* Negative class dominates
* Positive class is more important

---

## Key Takeaways

* Jaccard Index measures similarity between predicted and actual labels.
* It ranges from 0 to 1.
* Higher value means better model performance.
* It is widely used in ML evaluation.
* NumPy makes implementation faster and cleaner.
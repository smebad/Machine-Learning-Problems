# Implement Gini Impurity Calculation for a Set of Classes

## 1. Problem Overview

In machine learning, **Gini Impurity** is a metric used mainly in **Decision Tree algorithms** (such as CART) to measure how "pure" or "impure" a dataset is.

A dataset is considered **pure** if all the elements belong to the same class. If the dataset contains a mix of different classes, it is considered **impure**.

The goal of this problem is to implement a function that calculates the Gini Impurity for a given list of class labels.

---

## 2. What is Gini Impurity?

Gini Impurity answers the question:

> If we randomly pick an element from the dataset, what is the probability that it will be incorrectly classified?

The formula for Gini Impurity is:

Gini = 1 - Σ(pᵢ²)

Where:

* pᵢ is the probability of class i
* The summation is over all unique classes

### Example

Input:

```
y = [0, 1, 1, 1, 0]
```

Class probabilities:

* Class 0 → 2/5 = 0.4
* Class 1 → 3/5 = 0.6

Gini Impurity:

Gini = 1 - (0.4² + 0.6²)
Gini = 1 - (0.16 + 0.36)
Gini = 1 - 0.52 = 0.48

---

## 3. Code with Comments

```python
import numpy as np

def gini_impurity(y: list[int]) -> float:

    # Get all unique classes in the dataset
    classes = set(y)

    # Total number of samples
    n = len(y)

    # Variable to store sum of squared probabilities
    gini_impurity = 0

    # Loop through each unique class
    for cls in classes:
        # Count how many times this class appears
        # Divide by total samples to get probability
        gini_impurity += (y.count(cls)/n)**2

    # Final Gini Impurity formula
    return round(1 - gini_impurity, 3)

# Test Case
y = [0, 1, 1, 1, 0]
print(gini_impurity(y))  # Output: 0.48
```

---

## 4. Step-by-Step Logic

Let’s break the logic into simple steps:

1. **Find unique classes**

   * `set(y)` gives all distinct labels in the dataset.

2. **Count total samples**

   * `n = len(y)` stores how many items are in the dataset.

3. **Compute class probabilities**

   * For each class:

     * Count its occurrences
     * Divide by total samples

4. **Square the probabilities**

   * This emphasizes dominant classes

5. **Apply the Gini formula**

   * Subtract the sum of squared probabilities from 1

6. **Round result**

   * Output is rounded to 3 decimal places for readability

---

## 5. Why Gini Impurity is Important

Gini Impurity is heavily used in **Decision Trees** to:

* Decide the best feature to split on
* Measure how good a split is
* Try to create nodes with low impurity (more pure)

Lower Gini → better split
Higher Gini → more mixed classes

---

## 6. Time Complexity

This implementation uses:

* `y.count(cls)` inside a loop

So the time complexity is:

O(n × k)

Where:

* n = number of samples
* k = number of unique classes

For small datasets this is fine, but for large datasets this can be optimized.

---

## 7. Key Takeways

In simple words:

* Gini Impurity tells us how mixed a dataset is.
* If all values are same → Gini = 0 (perfectly pure)
* If values are evenly mixed → Gini is higher

This function:

* Finds class probabilities
* Squares them
* Subtracts from 1
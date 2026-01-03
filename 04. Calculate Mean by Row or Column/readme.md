# Calculate Mean by Row or Column

## 1. Problem Overview

### What Does "Calculate Mean by Row or Column" Mean?

In matrix operations, calculating the **mean** involves finding the average of a set of numbers. When working with matrices, we often need to compute averages either:

* **Row-wise**: average of each row
* **Column-wise**: average of each column

This operation is very common in machine learning and data analysis, especially during data preprocessing and feature analysis.

### Why Is This Important in Machine Learning?

* Feature normalization and scaling
* Understanding data distribution
* Aggregating values across samples or features

### The Problem

Write a Python function that:

* Takes a 2D matrix (list of lists)
* Takes a mode (`'row'` or `'column'`)
* Returns a list of mean values based on the selected mode

---

## 2. Code Explanation With Comments

Below is your provided solution with added comments to make the logic easy to remember.

```python
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    # If mode is 'column', compute the mean of each column
    if mode == 'column':
        # zip(*matrix) groups elements column-wise
        # sum(col) calculates the sum of one column
        # len(matrix) is the number of rows (used to compute mean)
        return [sum(col) / len(matrix) for col in zip(*matrix)]

    # If mode is 'row', compute the mean of each row
    elif mode == 'row':
        # sum(row) calculates the sum of one row
        # len(row) is the number of elements in that row
        return [sum(row) / len(row) for row in matrix]
```

### Key Things to Remember

* Column mean divides by the number of rows
* Row mean divides by the number of columns
* `zip(*matrix)` is used to access columns easily

---

## 3. Step-by-Step Solution Approach

### Case 1: Mean by Column

1. Use `zip(*matrix)` to group values column-wise
2. For each column:

   * Calculate the sum
   * Divide by the total number of rows
3. Store each result in a list

### Case 2: Mean by Row

1. Iterate through each row in the matrix
2. For each row:

   * Calculate the sum
   * Divide by the number of elements in the row
3. Store each result in a list

---

## 4. Understanding with an Example

### Input Matrix

```python
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
```

### Column Mean Calculation

* Column 1: (1 + 4 + 7) / 3 = 4.0
* Column 2: (2 + 5 + 8) / 3 = 5.0
* Column 3: (3 + 6 + 9) / 3 = 6.0

Output:

```python
[4.0, 5.0, 6.0]
```

### Row Mean Calculation

* Row 1: (1 + 2 + 3) / 3 = 2.0
* Row 2: (4 + 5 + 6) / 3 = 5.0
* Row 3: (7 + 8 + 9) / 3 = 8.0

Output:

```python
[2.0, 5.0, 8.0]
```

---

## 5. Why This Solution Works Well

* Uses Python built-in functions efficiently
* Avoids unnecessary nested loops
* Clear separation between row and column logic
* Easy to extend for other aggregation operations

---

## 6. Alternative Perspective

* **Row mean**: look left to right, then average
* **Column mean**: look top to bottom, then average

Both operations follow the same idea; only the direction changes.

---

## 7. Test Cases
```python
if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    # Test for column mean
    column_mean = calculate_matrix_mean(matrix, 'column')
    print("Column Mean:", column_mean)  # Output: [4.0, 5.0, 6.0]
    
    # Test for row mean
    row_mean = calculate_matrix_mean(matrix, 'row')
    print("Row Mean:", row_mean)  # Output: [2.0, 5.0, 8.0]
```

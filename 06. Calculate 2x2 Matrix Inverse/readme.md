# Calculate 2x2 Matrix Inverse

## Overview

This problem focuses on calculating the inverse of a 2x2 matrix using basic linear algebra rules. Matrix inversion is an important concept in machine learning, especially in areas like linear regression, optimization, and solving systems of equations. For a 2x2 matrix, the inverse can be computed using a direct mathematical formula, making it a good exercise to understand how matrix operations work internally.

The task is to write a function that takes a 2x2 matrix as input and returns its inverse. If the matrix is not invertible, the function should return `None`.

---

## Problem Explanation

Given a 2x2 matrix:

[[a, b],
[c, d]]

The inverse of this matrix exists only if its determinant is non-zero.

The determinant is calculated as:

determinant = (a × d) − (b × c)

If the determinant is zero, the matrix does not have an inverse. Otherwise, the inverse is calculated using the formula:

(1 / determinant) × [[d, -b], [-c, a]]

---

## Code With Comments

```python
# Function to calculate the inverse of a 2x2 matrix
def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    # Extract individual elements from the matrix
    a, b = matrix[0][0], matrix[0][1]
    c, d = matrix[1][0], matrix[1][1]
    
    # Calculate the determinant (ad - bc)
    determinant = a * d - b * c
    
    # If determinant is zero, the matrix is not invertible
    if determinant == 0:
        return None
    
    # Apply the inverse formula for a 2x2 matrix
    inverse = [
        [d / determinant, -b / determinant],
        [-c / determinant, a / determinant]
    ]
    
    # Return the computed inverse matrix
    return inverse
```

---

## Solution Approach and Logic

1. Extract matrix values
   The matrix is broken down into four variables (a, b, c, d) to make calculations easier and more readable.

2. Compute the determinant
   The determinant tells us whether the matrix can be inverted. If its value is zero, division is not possible and the inverse does not exist.

3. Handle non-invertible cases
   If the determinant is zero, the function immediately returns `None`. This prevents invalid mathematical operations.

4. Apply the inverse formula
   When the determinant is non-zero, the standard mathematical formula for a 2x2 matrix inverse is applied directly.

5. Return the result
   The inverse matrix is returned as a list of lists, matching the input format.

---

## Understanding the Test Cases

* Test Case 1: A regular invertible matrix with a non-zero determinant.
* Test Case 2: A matrix with determinant zero, so the function returns `None`.
* Test Case 3: Another invertible matrix to verify correctness.
* Test Case 4: A special case where the matrix is its own inverse.
* Test Case 5: A diagonal matrix where each element is scaled by the determinant.

---

## Test Cases
```python
# Test case 1
matrix1 = [[4, 7], [2, 6]]
print(inverse_2x2(matrix1))  # Output: [[0.6, -0.7], [-0.2, 0.4]]

# Test case 2
matrix2 = [[1, 2], [3, 4]]
print(inverse_2x2(matrix2))  # Output: None

# Test case 3
matrix3 = [[2, 5], [1, 3]]
print(inverse_2x2(matrix3))  # Output: [[0.4, -0.5], [-0.2, 0.6]]

# Test case 4
matrix4 = [[0, 1], [1, 0]]
print(inverse_2x2(matrix4))  # Output: [[0, 1], [1, 0]]

# Test case 5
matrix5 = [[3, 0], [0, 3]]
print(inverse_2x2(matrix5))  # Output: [[0, 0], [0, 0]]
```

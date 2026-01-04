# Scalar Multiplication of a Matrix

## 1. Problem Overview

### What is Scalar Multiplication of a Matrix?

Scalar multiplication is a basic linear algebra operation where **every element of a matrix is multiplied by a single number**, called a scalar.

If a matrix has dimensions **m × n**, the result of scalar multiplication will also be an **m × n matrix**, with each value scaled by the scalar.

### Why Is This Important in Machine Learning?

Scalar multiplication is widely used in machine learning and data processing:

* Feature scaling and normalization
* Weight updates during optimization
* Adjusting learning rates and coefficients

### The Problem

Write a Python function that:

* Takes a matrix (list of lists)
* Takes a scalar value
* Multiplies each element of the matrix by the scalar
* Returns the resulting matrix

---

## 2. Code With Comments
```python
def scalar_multiply(matrix: list[list[int | float]], scalar: int | float) -> list[list[int | float]]:
    # Loop through each row in the matrix
    # For each row, multiply every element by the scalar
    # Store the results in a new matrix
    return [[element * scalar for element in row] for row in matrix]
```

### Key Points to Remember

* The shape of the matrix does not change
* Each element is processed independently
* List comprehensions make the solution concise and readable

---

## 3. Step-by-Step Solution Logic

1. **Iterate Over Rows**

   * Access each row in the matrix one by one

2. **Iterate Over Elements in Each Row**

   * Multiply each element by the scalar

3. **Build a New Matrix**

   * Store the scaled rows in a new list

4. **Return the Result**

   * The output matrix has the same dimensions as the input matrix

---

## 4. Understanding with an Example

### Input

```python
matrix = [[1, 2],
          [3, 4]]
scalar = 2
```

### Calculation

* Row 1: [1 × 2, 2 × 2] → [2, 4]
* Row 2: [3 × 2, 4 × 2] → [6, 8]

### Output

```python
[[2, 4], [6, 8]]
```

---

## 5. Test Cases Explained

1. **Positive integers**

   * Multiplies all values normally

2. **Zero and negative values**

   * Preserves sign while scaling

3. **Floating-point numbers**

   * Works correctly with decimals

4. **Negative matrix values**

   * Each value is scaled independently

5. **Larger matrices**

   * Scales all elements while maintaining structure

---

## 6. Alternative Approach Without List Comprehension
```python
def scalar_multiply_manual(matrix, scalar):
    result = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(element * scalar)
        result.append(new_row)
    return result
```

---

## 7. Test Cases
```python
if __name__ == "__main__":
    # Test case 1
    matrix = [[1, 2], [3, 4]]
    scalar = 2
    result = scalar_multiply(matrix, scalar)
    print(result)  # Output: [[2, 4], [6, 8]]

    # Test case 2
    matrix = [[0, -1], [5, 3]]
    scalar = 2
    result = scalar_multiply(matrix, scalar)
    print(result)  # Output: [[0, -2], [10, 6]]

    # Test case 3
    matrix = [[1.5, 2.5], [3.5, 4.5]]
    scalar = 2
    result = scalar_multiply(matrix, scalar)
    print(result)  # Output: [[3.0, 5.0], [7.0, 9.0]]

    # Test case 4
    matrix = [[-1, -2], [-3, -4]]
    scalar = 2
    result = scalar_multiply(matrix, scalar)
    print(result)  # Output: [[2, 4], [6, 8]]

    # Test case 5
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    scalar = 3
    result = scalar_multiply(matrix, scalar)
    print(result)  # Output: [[3, 6, 9], [12, 15, 18], [21, 24, 27]]

```

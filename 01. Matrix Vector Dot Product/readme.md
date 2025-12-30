# Matrix-Vector Dot Product

## 1. Problem Overview

### What is a Matrix-Vector Dot Product?

A **matrix-vector dot product** is a fundamental operation in linear algebra and machine learning. It multiplies a matrix with a vector to produce a **new vector**.

* A **matrix** is a list of lists, where each inner list represents a row.
* A **vector** is a single list of numbers.

If the matrix has dimensions **n × m** (n rows and m columns), then the vector must have **m elements**. The result will be a vector of length **n**.

### Why is this important?

Matrix-vector multiplication is used everywhere in machine learning, such as:

* Linear regression
* Neural networks (forward pass)
* Feature transformations

### The Problem

Write a Python function that:

* Takes a matrix `a` and a vector `b`
* Returns the resulting vector if the dot product is valid
* Returns `-1` if the dimensions are incompatible

### Example

**Input**

```python
a = [[1, 2], [2, 4]]
b = [1, 2]
```

**Output**

```python
[5, 10]
```

**Explanation**

* Row 1: (1 × 1) + (2 × 2) = 5
* Row 2: (2 × 1) + (4 × 2) = 10

---

## 2. Code Explanation (With Comments)

Below is the same code you provided, rewritten with clear comments to help you remember the logic.

```python
def matrix_dot_vector(a: list[list[int | float]], b: list[int | float]) -> list[int | float]:
    # Check if matrix-vector multiplication is possible
    # Number of columns in matrix must equal length of vector
    if len(a[0]) != len(b):
        return -1

    # This will store the final resulting vector
    result = []

    # Loop through each row of the matrix
    for row in a:
        total = 0  # Stores dot product result for one row

        # Multiply each element of the row with the corresponding vector element
        for i in range(len(row)):
            total += row[i] * b[i]

        # Append the result for this row to the result vector
        result.append(total)

    return result
```

### Key Things to Remember

* Each row of the matrix produces **one number** in the output vector
* `total` resets for every row
* Multiplication happens element-by-element, then summed

---

## 3. Solution Approach and Logic

### Step-by-Step Approach

1. **Dimension Check**

   * Before multiplying, check if the operation is valid
   * Matrix columns must equal vector length

2. **Initialize Result List**

   * This will store the final output vector

3. **Row-wise Calculation**

   * Take one row at a time
   * Multiply each element of the row with the matching vector element
   * Add all products to get a single number

4. **Store the Result**

   * Append the computed value to the result list

5. **Return Output**

   * If all rows are processed successfully, return the result vector

---

## 4. Understanding the Logic with an Example

Matrix:

```text
[1  0  2]
[0  3 -1]
[4  1  0]
```

Vector:

```text
[3  5  2]
```

### Row-wise Calculation

* Row 1: (1×3) + (0×5) + (2×2) = 7
* Row 2: (0×3) + (3×5) + (-1×2) = 13
* Row 3: (4×3) + (1×5) + (0×2) = 17

Final Output:

```python
[7, 13, 17]
```

---

## 5. Why This Solution Works Well

* Uses basic loops (easy to understand)
* Avoids external libraries (good for learning fundamentals)
* Clearly follows the mathematical definition of dot product

---

## 6. Summary

* Matrix-vector dot product multiplies each matrix row with a vector
* The result is a new vector
* Dimension compatibility is critical
* This implementation is simple, readable, and educational

## 7. Test Cases
```python
if __name__ == "__main__":
    # Test case 1
    a = [[1, 2], [2, 4]]
    b = [1, 2]
    print(matrix_dot_vector(a, b))  # Output: [5, 10]

    # Test case 2
    a = [[1, 0, 2], [0, 3, -1], [4, 1, 0]]
    b = [3, 5, 2]
    print(matrix_dot_vector(a, b))  # Output: [7, 13, 17]

    # Test case 3
    a = [[1, 2, 3], [4, 5, 6]]
    b = [7, 8]
    print(matrix_dot_vector(a, b))  # Output: -1 (incompatible dimensions)

    # Test case 4
    a = [[0, -1], [1, 0]]
    b = [2, 3]
    print(matrix_dot_vector(a, b))  # Output: [-3, 2]

```

# Transpose of a Matrix

## 1. Problem Overview

### What is the Transpose of a Matrix?

The **transpose** of a matrix is an operation that flips a matrix over its diagonal. In simpler terms:

* Rows become columns
* Columns become rows

If the original matrix has dimensions **m × n**, the transpose will have dimensions **n × m**.

### Why is it important?

Matrix transposition is commonly used in machine learning and linear algebra for:

* Adjusting data shapes for matrix multiplication
* Computing covariance matrices
* Changing orientation of features in datasets

### The Problem

Write a Python function that:

* Takes a 2D matrix `a`
* Returns its transpose
* Works for any size matrix, including single-row or single-column matrices

### Example

**Input**

```python
a = [[1, 2, 3], [4, 5, 6]]
```

**Output**

```python
[[1, 4], [2, 5], [3, 6]]
```

**Explanation**

* Row 1 `[1, 2, 3]` becomes column 1
* Row 2 `[4, 5, 6]` becomes column 2
* Result is a 3 × 2 matrix

---

## 2. Code Explanation (With Comments)

Here is your code with detailed comments for clarity:

```python
def transpose_matrix(a: list[list[int | float]]) -> list[list[int | float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # zip(*a) takes all rows of the matrix and pairs elements by index
    # For example, first elements of all rows become first row of the transposed matrix
    # list(row) converts the tuples returned by zip into lists
    return [list(row) for row in zip(*a)]
```

### How It Works

* `*a` unpacks the matrix rows as separate arguments to `zip`
* `zip` groups elements from each row by their position
* Each grouped tuple corresponds to a row in the transposed matrix
* Convert tuples to lists to maintain consistent matrix structure

---

## 3. Step-by-Step Approach and Logic

1. **Understand the Shape**

   * Original matrix has m rows and n columns
   * Transposed matrix will have n rows and m columns

2. **Use `zip` for Pairing Elements**

   * `zip(*a)` pairs elements at the same index from all rows

3. **Convert Tuples to Lists**

   * `zip` returns tuples, but we usually represent matrices as lists of lists in Python

4. **Return the Transposed Matrix**

   * Collect all rows into a new matrix and return

### Visual Example

Matrix:

```text
[1 2 3]
[4 5 6]
```

Transpose:

```text
[1 4]
[2 5]
[3 6]
```

* Column 1 of transpose = Row 1 of original `[1, 4]`
* Column 2 of transpose = Row 2 of original `[2, 5]`
* Column 3 of transpose = Row 3 of original `[3, 6]`

---

## 4. Test Cases Explained

1. **2 × 3 matrix**

```python
[[1, 2, 3], [4, 5, 6]] -> [[1, 4], [2, 5], [3, 6]]
```

2. **3 × 2 matrix**

```python
[[7, 8], [9, 10], [11, 12]] -> [[7, 9, 11], [8, 10, 12]]
```

3. **1 × 1 matrix**

```python
[[1]] -> [[1]]
```

4. **4 × 2 matrix**

```python
[[1, 2], [3, 4], [5, 6], [7, 8]] -> [[1, 3, 5, 7], [2, 4, 6, 8]]
```

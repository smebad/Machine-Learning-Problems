# Reshape Matrix - LeetCode

## 1. Problem Overview

### What is Reshaping a Matrix?

Reshaping a matrix means **changing its number of rows and columns without changing the order of its elements**.

For example, a matrix with shape **2 × 4** contains 8 elements. These same 8 elements can be rearranged into a **4 × 2** matrix as long as the total number of elements remains the same.

### Why is this important in Machine Learning?

Matrix reshaping is very common in machine learning and data processing:

* Preparing data before feeding it into a model
* Converting between different data representations
* Adjusting batch sizes and feature dimensions

### The Problem

Write a Python function that:

* Takes a matrix `a`
* Takes a target shape `new_shape = (rows, columns)`
* Returns the reshaped matrix if possible
* Returns an empty list `[]` if reshaping is not possible

Reshaping is **only valid if**:

```
(total elements in original matrix) == (total elements in new shape)
```

---

## 2. Code With Comments

Below is your original solution with detailed comments added for clarity and memory aid.

```python
import numpy as np

def reshape_matrix(a: list[list[int | float]], new_shape: tuple[int, int]) -> list[list[int | float]]:
    # Check if reshaping is possible
    # Total elements in original matrix = rows * columns
    # Total elements in new shape = new_rows * new_columns
    if len(a) * len(a[0]) != new_shape[0] * new_shape[1]:
        return []  # Reshape not possible

    # Convert Python list to NumPy array
    # Use NumPy's reshape method
    # Convert back to list of lists before returning
    return np.array(a).reshape(new_shape).tolist()
```

### Key Points to Remember

* Reshape does NOT change element order
* Only the matrix shape changes
* NumPy handles the heavy lifting efficiently

---

## 3. Step-by-Step Solution Logic

1. **Count Total Elements**

   * Original matrix: `len(a) * len(a[0])`
   * Target matrix: `new_shape[0] * new_shape[1]`

2. **Validate Reshape Condition**

   * If counts are different, reshaping is impossible
   * Return `[]` immediately

3. **Use NumPy for Reshaping**

   * Convert matrix to NumPy array
   * Apply `.reshape(new_shape)`
   * Convert result back to Python list

4. **Return the Result**

---

## 4. Understanding with an Example

### Input

```python
a = [[1, 2, 3, 4],
     [5, 6, 7, 8]]
new_shape = (4, 2)
```

### Flattened Order (Internal View)

```text
1, 2, 3, 4, 5, 6, 7, 8
```

### Output

```python
[[1, 2],
 [3, 4],
 [5, 6],
 [7, 8]]
```

The numbers stay in the same order; only the row and column structure changes.

---

## 5. Test Cases

### Test Case 1

```python
[[1,2,3,4],[5,6,7,8]] → (4,2)
```

Valid because 2×4 = 4×2 = 8 elements

### Test Case 2

```python
[[1,2,3],[4,5,6]] → (3,2)
```

Valid because 2×3 = 3×2 = 6 elements

### Test Case 3

```python
[[1,2],[3,4]] → (4,2)
```

Invalid because 2×2 ≠ 4×2

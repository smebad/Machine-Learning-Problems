# Implement Compressed Row Sparse Matrix (CSR) Format Conversion

## 1. What is CSR Format and What Problem Does It Solve?

**Compressed Row Sparse (CSR) Format** is a way of storing a matrix efficiently when most of its values are zero.

Such matrices are called **sparse matrices**.

Example of a sparse matrix:

```
[
  [1, 0, 0, 0],
  [0, 2, 0, 0],
  [3, 0, 4, 0],
  [1, 0, 0, 5]
]
```

Most values are `0`, which waste memory if stored normally.

### The Problem CSR Solves

Storing a large sparse matrix in dense form:

* Uses a lot of memory
* Slows down computations

CSR solves this by:

* Storing only non-zero values
* Storing their column positions
* Keeping track of where each row starts

This reduces:

* Memory usage
* Computation time

CSR is widely used in:

* Scientific computing
* Graph algorithms
* Recommender systems
* Natural language processing

---

## 2. CSR Data Structures

CSR format stores a matrix using **three arrays**:

### 1. Values Array

Stores all non-zero elements row by row.

### 2. Column Indices Array

Stores the column index of each non-zero value.

### 3. Row Pointer Array

Stores cumulative counts of non-zero elements.
It tells where each row starts in the values array.

---

## 3. Code With Comments
```python
import numpy as np

# Function to convert dense matrix to CSR format
def compressed_row_sparse_matrix(dense_matrix):
    # Stores all non-zero values
    vals = []
    
    # Stores column index for each non-zero value
    col_idx = []
    
    # Stores start index of each row in vals
    # First value is always 0
    row_ptr = [0]

    # Loop through each row
    for row in dense_matrix:
        # Loop through each value with column index
        for j, val in enumerate(row):
            # If value is not zero
            if val != 0:
                # Store the value
                vals.append(val)
                
                # Store its column index
                col_idx.append(j)
        
        # After finishing the row,
        # append current length of vals
        # This marks the end of this row
        row_ptr.append(len(vals))

    return vals, col_idx, row_ptr

# Test Case
dense_matrix = [
    [1, 0, 0, 0],
    [0, 2, 0, 0],
    [3, 0, 4, 0],
    [1, 0, 0, 5]
]

vals, col_idx, row_ptr = compressed_row_sparse_matrix(dense_matrix)
print("Values array:", vals)
print("Column indices array:", col_idx)
print("Row pointer array:", row_ptr)
```

---

## 4. Step-by-Step Conversion Example

Given matrix:

```
[
 [1, 0, 0, 0],
 [0, 2, 0, 0],
 [3, 0, 4, 0],
 [1, 0, 0, 5]
]
```

### Values Array

Take all non-zero values row by row:

```
[1, 2, 3, 4, 1, 5]
```

### Column Indices Array

Store column positions of each value:

```
[0, 1, 0, 2, 0, 3]
```

### Row Pointer Array

Count how many values appear up to each row:

```
Row 0 starts at index 0
Row 1 starts at index 1
Row 2 starts at index 2
Row 3 starts at index 4
Row 4 ends at index 6
```

So:

```
[0, 1, 2, 4, 6]
```

---

## 5. Logic and Approach

The idea is simple:

1. Scan the matrix row by row
2. Whenever you see a non-zero value:

   * Save the value
   * Save its column index
3. After each row:

   * Save how many values you have stored so far

This allows you to reconstruct the original matrix later.

---

## 6. Why CSR Is Important in Machine Learning

CSR is used because:

* Many ML datasets are sparse
* It saves memory
* It speeds up matrix operations

Examples:

* Bag of Words
* TF-IDF matrices
* Graph adjacency matrices

---

## Key Takeaways

* CSR is an efficient way to store sparse matrices.
* It uses three arrays: values, column indices, row pointer.
* It avoids storing zeros.
* It is critical for scalable ML systems.
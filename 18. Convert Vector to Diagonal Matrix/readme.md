# Convert Vector to Diagonal Matrix

## Problem Overview

In machine learning and linear algebra, it is often necessary to transform a vector into a diagonal matrix. A diagonal matrix is a square matrix where all elements outside the main diagonal are zero, and the diagonal elements contain the values of the original vector.

The goal of this problem is to write a function that takes a one-dimensional NumPy array and converts it into a two-dimensional diagonal matrix, where each element of the input vector appears on the main diagonal.

---

## Why This Matters in Machine Learning

Diagonal matrices are commonly used in:

* Scaling features
* Representing variances in covariance matrices
* Linear transformations
* Optimization algorithms

Understanding how to construct them manually helps build a strong foundation in matrix operations used throughout machine learning.

---

## Example

### Input

```
x = np.array([1, 2, 3])
```

### Output

```
[[1. 0. 0.]
 [0. 2. 0.]
 [0. 0. 3.]]
```

Each value from the input vector is placed on the diagonal, and all other positions are filled with zeros.

---

## Solution Code with Comments

```python
import numpy as np

def make_diagonal(x):
    # Create an identity matrix of size equal to the number of elements in x
    # An identity matrix has 1s on the diagonal and 0s elsewhere
    identity_matrix = np.identity(np.size(x))

    # Multiply the identity matrix with the vector x
    # NumPy broadcasts x across rows, placing each value on the diagonal
    return identity_matrix * x
```

---

## How the Solution Works

1. The size of the input vector `x` is determined using `np.size(x)`.
2. An identity matrix of shape `(n, n)` is created, where `n` is the length of the vector.
3. The identity matrix is multiplied by the vector `x`.
4. Due to NumPy broadcasting, each diagonal `1` in the identity matrix is replaced by the corresponding value from `x`.
5. All non-diagonal elements remain `0`.

---

## Test Case

```python
x = np.array([1, 2, 3])
output = make_diagonal(x)
print(output)
```

### Output

```
[[1. 0. 0.]
 [0. 2. 0.]
 [0. 0. 3.]]
```

---

## Key Takeaways

* A diagonal matrix stores vector values along its main diagonal
* Identity matrices play a key role in constructing diagonal matrices
* Understanding broadcasting helps in writing efficient NumPy code
* Learning the manual approach improves intuition for matrix operations

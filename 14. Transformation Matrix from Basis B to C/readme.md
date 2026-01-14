# Transformation Matrix from Basis B to C

## 1. Problem Overview

In linear algebra and machine learning, changing the representation of vectors between different coordinate systems (bases) is a very common task. A **transformation matrix from basis B to basis C** allows us to convert the coordinates of a vector expressed in basis B into coordinates expressed in basis C.

The problem is to compute this transformation matrix given two different bases **B** and **C** for R^3. Each basis is provided as a 3×3 matrix, where each column (or row, depending on convention) represents a basis vector.

This concept is important in areas such as feature space transformations, dimensionality reduction, graphics, and numerical linear algebra.

---

## 2. Mathematical Idea

If a vector ( v ) is represented in basis **B**, and we want to express the same vector in basis **C**, we use the following relationship:

[
P = C^{-1} B
]

Where:

* ( B ) is the matrix whose columns are the basis vectors of basis B
* ( C ) is the matrix whose columns are the basis vectors of basis C
* ( C^{-1} ) is the inverse of matrix C
* ( P ) is the transformation matrix from basis B to basis C

Once ( P ) is computed, multiplying it with coordinates in basis B gives the coordinates in basis C.

---

## 3. Code With Comments
```python
import numpy as np

def transform_basis(B, C):
    # Convert the input lists into NumPy arrays
    # This allows us to use matrix operations like inverse and dot product
    C = np.array(C)
    B = np.array(B)

    # Compute the inverse of matrix C
    # This is required to change coordinates from basis B to basis C
    C_inv = np.linalg.inv(C)

    # Multiply C inverse with B to get the transformation matrix
    # P = C^{-1} * B
    P = np.dot(C_inv, B)

    # Convert the result back to a Python list for clean output
    return P.tolist()
```

---

## 4. Step-by-Step Approach and Logic

1. **Convert input to matrices**
   The bases B and C are given as Python lists. NumPy arrays are used to easily perform linear algebra operations.

2. **Invert matrix C**
   To move from basis B to basis C, we need the inverse of C. This step is only possible if C is invertible.

3. **Matrix multiplication**
   The transformation matrix is computed using the formula:

   [
   P = C^{-1} B
   ]

4. **Return readable output**
   The result is converted back to a list so it is easy to print or use elsewhere.

---

## 5. Test Case

```python
B = [[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]]

C = [[1, 2.3, 3],
     [4.4, 25, 6],
     [7.4, 8, 9]]

print(transform_basis(B, C))
```

**Expected Output:**

```text
[[-0.6772, -0.0126, 0.2342],
 [-0.0184, 0.0505, -0.0275],
 [0.5732, -0.0345, -0.0569]]
```

---

## 6. Understanding the Result

* Each column of the transformation matrix tells how a basis vector of **B** is represented in basis **C**.
* The matrix works as a converter between coordinate systems.
* Small decimal values appear because the transformation involves matrix inversion.

---

## 7. Key Takeaways

* A basis defines how vectors are represented in a space.
* Changing bases requires matrix inversion and multiplication.
* The formula ( C^{-1} B ) is fundamental for coordinate transformations.

* NumPy makes linear algebra operations concise and reliable.

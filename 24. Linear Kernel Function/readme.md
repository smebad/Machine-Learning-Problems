# Linear Kernel Function

## 1. Problem Overview

In machine learning, especially in algorithms like Support Vector Machines (SVM), kernel functions are used to measure similarity between two data points. The **linear kernel** is the simplest kernel and is based on the dot product of two vectors.

The goal of this problem is to compute the linear kernel between two input vectors. This means multiplying corresponding elements of the vectors and summing the results.

---

## 2. What is a Linear Kernel

The linear kernel between two vectors x1 and x2 is defined as:

K(x1, x2) = x1 · x2

This is just the dot product. It measures how aligned two vectors are. If they point in a similar direction, the value is large. If they are perpendicular, the value is zero.

---

## 3. Code With Comments

Below is the given solution with added comments to make it easy to remember.

```python
import numpy as np

def kernel_function(x1, x2):
    # np.inner computes the dot product between two vectors
    # It multiplies corresponding elements and sums them
    # Example: [1,2,3] and [4,5,6] -> 1*4 + 2*5 + 3*6
    return np.inner(x1, x2)
```

---

## 4. Step by Step Logic

1. Two vectors x1 and x2 are given as NumPy arrays.
2. The inner product (dot product) is computed using NumPy.
3. Each element of x1 is multiplied by the corresponding element of x2.
4. All these products are added together.
5. The final number is returned as the kernel value.

---

## 5. Test Case

```python
x1 = np.array([1, 2, 3])
x2 = np.array([4, 5, 6])

result = kernel_function(x1, x2)
print(result)
```

Expected output:

32

Because:

1×4 + 2×5 + 3×6 = 4 + 10 + 18 = 32

---

## 6. Why Linear Kernel Is Useful

* It is fast and simple.
* It works well when data is already linearly separable.
* It does not require transforming data into higher dimensions.

---

## 7. Key Takeaways

* A kernel measures similarity between two vectors.
* The linear kernel is just the dot product.
* It is commonly used in linear models and SVMs.
* NumPy provides a simple way to compute it using np.inner.
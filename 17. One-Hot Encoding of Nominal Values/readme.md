# One-Hot Encoding of Nominal Values

## 1. Problem Overview

In machine learning, many algorithms require numerical input. However, real-world datasets often contain **categorical (nominal) values**, such as class labels or category IDs. One-hot encoding is a common technique used to convert these categorical values into a numerical format that machine learning models can understand.

The goal of this problem is to implement **one-hot encoding** for a 1D NumPy array of integer values. Each integer represents a category, and the output should be a binary matrix where each row corresponds to one input value and contains exactly one `1`, indicating the category, and `0`s elsewhere.

The function should also support an optional parameter to manually specify the number of output columns.

---

## 2. What Is One-Hot Encoding?

One-hot encoding transforms a categorical value into a vector of binary values:

* The length of the vector equals the number of categories
* The index corresponding to the category is set to `1`
* All other indices are set to `0`

For example:

```
Category 2 with 3 total categories -> [0, 0, 1]
```

This representation avoids introducing unintended ordinal relationships between categories.

---

## 3. Code Explanation Comments
```python
import numpy as np

def to_categorical(x, n_col=None):
    # If number of columns is not provided
    # infer it from the maximum value in x
    if not n_col:
        n_col = np.amax(x) + 1

    # Initialize a matrix of zeros
    # Rows = number of samples
    # Columns = number of categories
    one_hot = np.zeros((x.shape[0], n_col))

    # Set the appropriate index in each row to 1
    # np.arange(x.shape[0]) gives row indices
    # x gives the column index for each row
    one_hot[np.arange(x.shape[0]), x] = 1

    return one_hot
```

---

## 4. Step-by-Step Approach and Logic

1. **Determine number of categories**
   If `n_col` is not provided, it is calculated as `max(x) + 1` because categories are zero-indexed.

2. **Create a zero matrix**
   A matrix of shape `(number of samples, number of categories)` is initialized with zeros.

3. **Assign ones using indexing**
   For each input value, the corresponding column index is set to `1` in that row.

4. **Return encoded matrix**
   The final matrix represents the one-hot encoded form of the input data.

---

## 5. Test Case

```python
x = np.array([0, 1, 2, 1, 0])
output = to_categorical(x)
print(output)
```

**Output:**

```text
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]
 [0. 1. 0.]
 [1. 0. 0.]]
```

---

## 6. Understanding the Result

* Each row corresponds to one value in the input array
* Each column represents a category
* Exactly one `1` appears in each row
* The output is suitable for use in classification models

---

## 7. Key Takeaways

* One-hot encoding is essential for handling categorical data
* It prevents models from assuming numeric order between categories
* NumPy indexing makes the implementation efficient and clean
* This technique is widely used in classification and neural networks
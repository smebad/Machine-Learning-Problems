# Batch Iterator for Dataset

## 1. Problem Overview

In machine learning, datasets are often too large to be processed all at once. Instead, data is divided into smaller chunks called **batches**, which are processed one at a time. This technique is widely used in training algorithms such as gradient descent and neural networks.

The goal of this problem is to implement a **batch iterator** that splits a dataset into smaller batches of a given size. The function should work with:

* Only feature data `X`, or
* Both feature data `X` and target labels `y`, while preserving their correspondence

If the total number of samples is not perfectly divisible by the batch size, the last batch should contain the remaining samples.

---

## 2. Why Batch Iteration Is Important

Batch processing helps to:

* Reduce memory usage
* Improve computational efficiency
* Enable training on large datasets
* Stabilize learning during optimization

Almost all modern machine learning frameworks rely on batching internally.

---

## 3. Code With Comments

Below is the provided solution with added comments to clearly explain each step.

```python
import numpy as np

def batch_iterator(X, y=None, batch_size=64):
    # Get the total number of samples in the dataset
    n_samples = X.shape[0]

    # List to store all batches
    batches = []

    # Loop over the dataset in steps of batch_size
    for i in np.arange(0, n_samples, batch_size):
        # Define the start and end indices of the current batch
        begin = i
        end = min(i + batch_size, n_samples)

        # If labels are provided, return (X, y) pairs
        if y is not None:
            batches.append([X[begin:end], y[begin:end]])
        else:
            # Otherwise, return only feature batches
            batches.append(X[begin:end])

    return batches
```

---

## 4. Step-by-Step Approach and Logic

1. **Determine dataset size**
   The number of samples is obtained from the first dimension of `X`.

2. **Iterate in batch-sized steps**
   The loop advances by `batch_size` at each step to define batch boundaries.

3. **Handle the last batch safely**
   `min(i + batch_size, n_samples)` ensures the function does not exceed dataset limits.

4. **Maintain feature-label alignment**
   When `y` is provided, both `X` and `y` are sliced using the same indices.

5. **Store each batch**
   Each batch is appended to a list and returned at the end.

---

## 5. Test Case

```python
X = np.array([[1, 2],
              [3, 4],
              [5, 6],
              [7, 8],
              [9, 10]])

y = np.array([1, 2, 3, 4, 5])

batches = batch_iterator(X, y, batch_size=2)
print(batches)
```

### Output Explanation

* Batch 1: samples 0–1
* Batch 2: samples 2–3
* Batch 3: remaining sample

Each batch preserves the correct pairing between `X` and `y`.

---

## 6. Understanding the Output Structure

When labels are provided, each batch looks like:

```
[X_batch, y_batch]
```

If labels are not provided, only `X_batch` is returned.

---

## 7. Key Takeaways

* Batching is essential for scalable machine learning
* Always keep features and labels aligned during shuffling or batching
* The final batch may be smaller than the specified batch size
* This pattern is foundational for training neural networks and optimizers
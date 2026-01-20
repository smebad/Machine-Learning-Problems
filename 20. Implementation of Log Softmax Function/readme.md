# Implementation of Log Softmax Function

## 1. Problem Overview

In machine learning, models often produce raw output values called **scores** or **logits**. These scores are not probabilities and cannot be directly interpreted. To convert them into probabilities, the **softmax function** is commonly used.

The **log-softmax function** is simply the logarithm of the softmax output. Instead of computing softmax first and then taking the log, log-softmax computes this in a more numerically stable way. This is especially important when dealing with large values, where direct exponentiation can cause overflow.

The goal of this problem is to implement the **log-softmax function from scratch** for a 1D NumPy array of scores.

---

## 2. What Is Log-Softmax?

Given a vector of scores:

[
\text{scores} = [x_1, x_2, ..., x_n]
]

The softmax function is defined as:

[
\text{softmax}(x_i) = \frac{e^{x_i}}{\sum_j e^{x_j}}
]

The log-softmax function is:

[
\log(\text{softmax}(x_i)) = x_i - \log\left(\sum_j e^{x_j}\right)
]

This form allows us to compute log-softmax efficiently and safely without explicitly computing softmax probabilities.

---

## 3. Code With Comments

```python
import numpy as np

def log_softmax(scores: list) -> np.ndarray:
    # Subtract the maximum score from all values
    # This improves numerical stability and prevents overflow
    scores = scores - np.max(scores)

    # Compute the log-softmax using the stable formula:
    # log_softmax(x) = x - log(sum(exp(x)))
    return scores - np.log(np.sum(np.exp(scores)))
```

---

## 4. Step-by-Step Approach and Logic

1. **Input scores**  
   The function takes a 1D NumPy array of raw scores (logits).

2. **Numerical stability trick**  
   The maximum value of the array is subtracted from all elements. This does not change the final result but prevents very large exponent values.

3. **Exponentiation and summation**  
   The exponential of each adjusted score is computed and summed.

4. **Log transformation**  
   The logarithm of the sum of exponentials is calculated.

5. **Final log-softmax output**  
   Each score is adjusted using the formula:

   [
   x_i - \log\left(\sum_j e^{x_j}\right)
   ]

---

## 5. Example Walkthrough

**Input:**

```python
A = np.array([1, 2, 3])
```

**Step 1: Subtract max value (3)**

```text
[-2, -1, 0]
```

**Step 2: Apply log-softmax formula**

The result becomes:

```text
[-2.4076, -1.4076, -0.4076]
```

These values represent the logarithm of the softmax probabilities.

---

## 6. Alternative (Naive) Approach and Why It Is Worse

A naive implementation would be:

```python
softmax = np.exp(scores) / np.sum(np.exp(scores))
log_softmax = np.log(softmax)
```

### Why this is not ideal:

* Computing `np.exp(scores)` directly can overflow for large values
* It performs unnecessary operations
* Less efficient and less stable

The provided solution avoids these problems by combining steps into a single stable formula.

---

## 7. Time and Space Complexity

* **Time Complexity:** O(n)  
  Each element in the array is processed once.

* **Space Complexity:** O(n)  
  A new array is created for the output.

---

## 8. Key Takeaways

* Log-softmax is commonly used in classification models with cross-entropy loss
* Subtracting the maximum value improves numerical stability
* Implementing log-softmax directly is better than using softmax followed by log
* Understanding this function helps in learning neural network loss functions
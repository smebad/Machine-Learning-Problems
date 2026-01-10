# Sigmoid Activation Function Understanding

## 1. Problem Overview

### What is the Sigmoid Activation Function?

The sigmoid activation function is a mathematical function commonly used in machine learning and neural networks. It takes any real-valued number as input and maps it to a value between 0 and 1. Because of this property, sigmoid is often used in binary classification problems where outputs represent probabilities.

The sigmoid function is defined as:

```
σ(z) = 1 / (1 + e^(-z))
```

### The Problem

Write a Python function that:

* Takes a single numeric input `z`
* Computes the sigmoid activation value using the formula
* Returns the result rounded to four decimal places

---

## 2. Code Explanation With Comments

```python
import math

def sigmoid(z: float) -> float:
    # Apply the sigmoid formula
    result = 1 / (1 + math.exp(-z))

    # Round the result to 4 decimal places
    return round(result, 4)
```

### Key Points to Remember

* `math.exp(-z)` computes e raised to the power `-z`.
* The denominator ensures the output stays between 0 and 1.
* Rounding helps handle floating-point precision.

---

## 3. Solution Approach and Logic

1. **Compute the exponential term**

   * Calculate `exp(-z)` using the math library.

2. **Apply the sigmoid formula**

   * Add 1 to the exponential value.
   * Divide 1 by the result to get the sigmoid output.

3. **Round the output**

   * Limit the result to four decimal places for consistency and readability.

---

## 4. Example Walkthrough

### Input

```python
z = 0
```

### Calculation

* `exp(-0) = 1`
* `1 / (1 + 1) = 0.5`

### Output

```python
0.5
```

---

## 5. Test Cases

```python
# Test Case 1
z = 0
print(sigmoid(z))  # Output: 0.5

# Test Case 2
z = 2
print(sigmoid(z))  # Output: 0.8808

# Test Case 3
z = -2
print(sigmoid(z))  # Output: 0.1192
```

These test cases show how the sigmoid function behaves:

* Near 0, output is close to 0.5
* Large positive values approach 1
* Large negative values approach 0

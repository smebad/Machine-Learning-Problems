# Linear Regression Using Gradient Descent

## 1. Problem Overview

### What is Linear Regression Using Gradient Descent?

Linear regression is used to model the relationship between a set of features and a target variable. Gradient descent is an iterative optimization algorithm used to find the coefficients (weights) of a linear model that minimize the cost function (mean squared error).

Unlike the normal equation, gradient descent does not require matrix inversion and is suitable for large datasets.

### The Problem

Write a Python function that:

* Takes `X` (feature matrix with a column of ones for intercept) and `y` (target vector)
* Performs gradient descent with a learning rate `alpha` and a specified number of iterations
* Returns the regression coefficients rounded to four decimal places

---

## 2. Code Explanation With Comments

```python
import numpy as np

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    m, n = X.shape              # m = number of samples, n = number of features
    y = y.reshape(-1, 1)       # Reshape y to be a column vector
    theta = np.zeros((n, 1))   # Initialize coefficients with zeros

    for _ in range(iterations):
        predictions = X @ theta             # Compute predicted values
        errors = predictions - y           # Compute prediction errors
        gradient = alpha * (X.T @ errors) / m   # Compute gradient of the cost function
        theta -= gradient                   # Update coefficients

    return np.round(theta.flatten(), 4)     # Flatten and round coefficients
```

### Key Points to Remember

* `X @ theta` performs matrix multiplication to get predictions.
* `errors` is the difference between predicted and actual values.
* `gradient` computes how much to adjust each coefficient.
* `theta -= gradient` updates coefficients in the direction that reduces error.
* Rounding handles numerical precision; `-0.0` is valid.

---

## 3. Solution Approach and Logic

1. **Initialize coefficients (`theta`) to zeros**

   * Starting point for gradient descent.

2. **Iteratively update coefficients**

   * Compute predictions using current coefficients.
   * Calculate the difference between predictions and actual targets.
   * Compute the gradient (partial derivative of the cost function).
   * Update coefficients by subtracting the scaled gradient.

3. **Repeat for the specified number of iterations**

   * Converges to coefficients that minimize the mean squared error.

4. **Return rounded coefficients**

   * Flatten the result to a 1D array for easier interpretation.

---

## 4. Example Calculation

### Input

```python
X = np.array([[1, 1], [1, 2], [1, 3]])
y = np.array([1, 2, 3])
alpha = 0.01
iterations = 1000
```

### Step-by-Step

* Start with `theta = [0, 0]`
* Compute predictions and errors.
* Calculate gradient: adjusts coefficients towards minimizing mean squared error.
* Repeat for 1000 iterations.
* Final `theta` approximately `[0.1107, 0.9513]` after rounding.

### Output

```python
[0.1107, 0.9513]
```

---

## 5. Test Cases

* **Test Case 1:** Small dataset with perfect linear relationship
* **Test Case 2:** Different feature offsets with perfect slope
* **Test Case 3:** Larger input values to test convergence

```python
if __name__ == "__main__":
    # Test Case 1
    X = np.array([[1, 1], [1, 2], [1, 3]])
    y = np.array([1, 2, 3])
    alpha = 0.01
    iterations = 1000
    coefficients = linear_regression_gradient_descent(X, y, alpha, iterations)
    print(coefficients)

    # Test Case 2
    X = np.array([[1, 0], [1, 1], [1, 2]])
    y = np.array([1, 2, 3])
    coefficients = linear_regression_gradient_descent(X, y, alpha, iterations)
    print(coefficients)

    # Test Case 3
    X = np.array([[1, 2], [1, 3], [1, 4]])
    y = np.array([2, 3, 4])
    coefficients = linear_regression_gradient_descent(X, y, alpha, iterations)
    print(coefficients)
```
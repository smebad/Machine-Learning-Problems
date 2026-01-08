# Linear Regression Using Gradient Descent
# Solution:
import numpy as np
def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    m, n = X.shape
    y = y.reshape(-1, 1)    
    theta = np.zeros((n, 1)) 

    for _ in range(iterations):
        predictions = X @ theta                 
        errors = predictions - y                
        gradient = alpha * (X.T @ errors) / m   
        theta -= gradient        

    return np.round(theta.flatten(), 4)

# Test Cases
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
    alpha = 0.01
    iterations = 1000
    coefficients = linear_regression_gradient_descent(X, y, alpha, iterations)
    print(coefficients)

    # Test Case 3
    X = np.array([[1, 2], [1, 3], [1, 4]])
    y = np.array([2, 3, 4])
    alpha = 0.01
    iterations = 1000
    coefficients = linear_regression_gradient_descent(X, y, alpha, iterations)
    print(coefficients)

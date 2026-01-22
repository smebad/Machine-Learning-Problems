# Implement Ridge Regression Loss Function

## 1. Problem Overview

Ridge Regression is a regularized version of linear regression. While standard linear regression tries to minimize the prediction error, Ridge Regression also adds a penalty for large model weights. This helps prevent overfitting and makes the model more stable when features are correlated.

The goal of this problem is to compute the **Ridge loss**, which combines two parts:

* Mean Squared Error (MSE), which measures how far predictions are from the true values.
* A regularization term, which penalizes large weight values.

This loss function is used during training to find the best weights for a Ridge Regression model.

---

## 2. Mathematical Formulation

The Ridge Regression loss is defined as:

L = MSE + alpha * sum(w^2)

Where:

* MSE = mean((y_true − y_pred)^2)
* y_pred = X · w
* alpha controls how strong the regularization is
* w is the vector of model weights

The first part measures prediction error, and the second part discourages large weights.

---

## 3. Code With Comments

```python
import numpy as np

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
    # X is the feature matrix where each row is one data sample
    # w is the weight vector (model parameters)
    # y_true contains the true target values
    # alpha controls the strength of regularization

    # Compute predictions using matrix multiplication: y_pred = X @ w
    predictions = X @ w

    # Compute the Mean Squared Error (MSE)
    # We subtract predictions from true values, square them, and take the average
    mse = np.mean((y_true - predictions) ** 2)

    # Compute the regularization term
    # This is the sum of squared weights multiplied by alpha
    regularization = alpha * np.sum(w ** 2)

    # The total Ridge loss is MSE plus the regularization term
    loss = mse + regularization

    return loss
```

---

## 4. Step-by-Step Logic

1. **Compute predictions**
   Multiply the feature matrix X with the weight vector w to get predicted values.

2. **Calculate error**
   Subtract predicted values from true values to see how wrong the model is.

3. **Square and average**
   Squaring ensures all errors are positive and emphasizes larger mistakes. Taking the mean gives the MSE.

4. **Add regularization**
   The sum of squared weights is added to discourage large coefficients.

5. **Return total loss**
   The final Ridge loss combines prediction error and weight penalty.

---

## 5. Test Case

```python
X = np.array([[1, 1], [2, 1], [3, 1], [4, 1]])
w = np.array([0.2, 2])
y_true = np.array([2, 3, 4, 5])
alpha = 0.1

loss = ridge_loss(X, w, y_true, alpha)
print(loss)
```

Expected output:

```
2.204
```

---

## 6. Why Ridge Loss Is Useful

In standard linear regression, the model may learn very large weights to fit the training data perfectly. This often leads to poor performance on new data. Ridge Regression fixes this by penalizing large weights, making the model simpler and more generalizable.

---

## 7. Key Takeaways

* MSE measures how wrong the predictions are.
* Regularization prevents the model from becoming too complex.
* Ridge loss is MSE plus a penalty for large weights.
* The alpha value controls how strong the penalty is.
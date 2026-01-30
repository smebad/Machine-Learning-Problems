# Calculate R-squared for Regression Analysis

## 1. Problem Overview

R-squared (also known as the **coefficient of determination**) is a popular evaluation metric used in regression problems. It measures how well a regression model explains the variability of the target variable.

In simple terms, R-squared answers the question:

> How much of the change in the output variable can be explained by the model?

The value of R-squared lies between:

* **1.0** → Perfect model (all predictions are correct)
* **0.0** → Model explains none of the variance
* Can be **negative** → Model performs worse than predicting the mean

### Problem Statement

You are given:

* `y_true`: Actual values
* `y_pred`: Predicted values

Your task is to compute the R-squared score using the formula:

R² = 1 - (SSR / SST)

Where:

* SSR (Sum of Squared Residuals) = Σ(y_true - y_pred)²
* SST (Total Sum of Squares) = Σ(y_true - mean(y_true))²

---

## 2. Code with Comments

```python
import numpy as np

def r_squared(y_true, y_pred):
    # If predictions are exactly equal to true values,
    # the model is perfect
    if np.array_equal(y_true, y_pred):
        return 1.0

    # Mean of true values
    y_mean = np.mean(y_true)

    # SSR: Sum of squared residuals (errors)
    ssr = np.sum((y_true - y_pred) ** 2)

    # SST: Total sum of squares
    sst = np.sum((y_true - y_mean) ** 2)

    try:
        # R-squared formula
        r2 = 1 - (ssr / sst)

        # Handle infinite values
        if np.isinf(r2):
            return 0.0

        # Round result to 3 decimal places
        return round(r2, 3)

    except ZeroDivisionError:
        # If all y_true values are the same
        return 0.0
```

---

## 3. Step-by-Step Explanation

### Step 1: Perfect Prediction Check

```python
if np.array_equal(y_true, y_pred):
    return 1.0
```

If the predictions are exactly equal to true values, then the model explains 100% of the variance.

---

### Step 2: Compute Mean of True Values

```python
y_mean = np.mean(y_true)
```

This represents a baseline model that predicts the same constant value for every sample.

---

### Step 3: Compute SSR (Error)

```python
ssr = np.sum((y_true - y_pred) ** 2)
```

This measures how far the predictions are from actual values.
Smaller SSR means better predictions.

---

### Step 4: Compute SST (Total Variance)

```python
sst = np.sum((y_true - y_mean) ** 2)
```

This measures how much variation exists in the dataset.

---

### Step 5: Apply R-squared Formula

```python
r2 = 1 - (ssr / sst)
```

This compares the model error against total variance.

---

## 4. Logic Behind R-squared

R-squared compares two things:

* How bad is the model? (SSR)
* How hard is the problem? (SST)

If SSR is very small compared to SST, then:

R² ≈ 1 → very good model

If SSR is similar to SST, then:

R² ≈ 0 → model is useless

If SSR is bigger than SST, then:

R² < 0 → model is worse than guessing

---

## 5. Why This Implementation Is Good

This solution:

* Works for any regression output
* Handles edge cases safely
* Avoids division by zero
* Returns clean rounded output

It is mathematically identical to sklearn's `r2_score` but implemented from scratch.

---

## 6. Common Mistakes

1. Forgetting to subtract the mean in SST
2. Using absolute error instead of squared error
3. Not handling the case where all y values are same
4. Assuming R-squared is always between 0 and 1

---

## 7. Real-World Usage

R-squared is widely used in:

* Linear regression
* Polynomial regression
* Financial forecasting
* Sales prediction
* Scientific modeling

It helps answer whether a model is actually learning meaningful patterns or not.

---

## 8. Key Takeaway

R-squared tells you how much of the problem your model has solved.
Higher R-squared → Better explanation power
Lower R-squared → Weak or useless model
It is one of the most important regression evaluation metrics in machine learning.
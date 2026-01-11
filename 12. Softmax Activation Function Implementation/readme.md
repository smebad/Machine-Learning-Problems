# Softmax Activation Function Implementation

## 1. Problem Overview

The **Softmax Activation Function** is commonly used in machine learning and deep learning models, especially in multi-class classification problems. Its main purpose is to convert a list of raw scores (also called logits) into a probability distribution.

### Why Softmax is Needed

Machine learning models often produce raw numerical scores that are difficult to interpret directly. These scores:

* Can be negative or positive
* Do not sum to 1
* Cannot be interpreted as probabilities

Softmax solves this problem by:

* Converting all values into positive numbers using the exponential function
* Scaling them so that their sum becomes exactly 1

This makes the output easy to interpret as probabilities for each class.

---

## 2. Code Explanation with Comments

Below is the same solution with detailed comments added to help remember each step of the logic.

```python
import math

def softmax(scores: list[float]) -> list[float]:
    # Step 1: Apply exponential to each score
    # This ensures all values become positive
    exp_scores = [math.exp(score) for score in scores]

    # Step 2: Compute the sum of all exponential values
    # This will be used for normalization
    sum_exp_scores = sum(exp_scores)

    # Step 3: Divide each exponential score by the total sum
    # This converts values into probabilities
    probabilities = [round(score / sum_exp_scores, 4) for score in exp_scores]

    # Step 4: Return the final probability distribution
    return probabilities
```

---

## 3. Solution Approach and Logic

### Step-by-Step Approach

1. **Exponentiation**
   Each input score is passed through the exponential function. Larger scores grow faster, which increases their influence on the final result.

2. **Normalization**
   All exponential values are summed together. Each value is then divided by this total to ensure that the final outputs sum to 1.

3. **Probability Output**
   The final result is a list of probabilities, where:

   * All values are between 0 and 1
   * The total sum of all values is exactly 1

4. **Rounding**
   The probabilities are rounded to four decimal places to match the problem requirements.

---

## 4. Understanding the Test Cases

### Test Case 1

```python
scores = [1, 2, 3]
```

* Higher score results in higher probability
* Output shows increasing probability values

### Test Case 2

```python
scores = [5, 10, 15]
```

* Very large difference between values
* Softmax strongly favors the largest score
* Smaller values approach zero

### Test Case 3

```python
scores = [0, 0, 0]
```

* All scores are equal
* Softmax distributes probability equally
* Each value becomes 1/3

---

## 5. Key Takeaways

* Softmax converts raw model outputs into probabilities
* It is mainly used in multi-class classification tasks
* Larger input values receive higher probabilities
* Equal inputs result in equal probabilities
* Rounding is applied only for final presentation
# Single Neuron

## 1. Problem Overview

A **single neuron** is the most basic building block of a neural network. It takes multiple input features, multiplies each feature by a corresponding weight, adds a bias, and then passes the result through an activation function to produce an output.

In this problem, we simulate a single neuron for **binary classification** using the **sigmoid activation function**. The goal is to:

* Compute predicted probabilities for each input sample
* Measure how accurate those predictions are using **Mean Squared Error (MSE)**

This helps in understanding how neural networks make predictions and how error is calculated during training.

---

## 2. Code Explanation (With Comments)

```python
import math

def single_neuron_model(features, labels, weights, bias):
    probabilities = []
    
    # Loop through each input feature vector
    for feature_vector in features:
        # Compute weighted sum (dot product) and add bias
        z = sum(weight * feature for weight, feature in zip(weights, feature_vector)) + bias
        
        # Apply sigmoid activation function
        prob = 1 / (1 + math.exp(-z))
        
        # Store rounded probability
        probabilities.append(round(prob, 4))
    
    # Calculate Mean Squared Error (MSE)
    mse = sum((prob - label) ** 2 for prob, label in zip(probabilities, labels)) / len(labels)
    mse = round(mse, 4)
    
    return probabilities, mse
```

---

## 3. Approach and Logic

### Step 1: Weighted Sum

Each input sample contains multiple features. For a single neuron, we calculate a weighted sum:

z = (w1 * x1) + (w2 * x2) + ... + bias

This combines the input features into a single value.

---

### Step 2: Sigmoid Activation

The weighted sum is passed through the sigmoid function:

σ(z) = 1 / (1 + e^(-z))

This converts the value into a probability between 0 and 1, which is useful for binary classification.

---

### Step 3: Prediction Storage

Each predicted probability is rounded to four decimal places and stored in a list.

---

### Step 4: Error Calculation (MSE)

Mean Squared Error measures how far predictions are from actual labels:

MSE = average of (prediction − actual label)²

A smaller MSE means better predictions.

---

## 4. Understanding the Output

For each input sample:

* A probability is produced showing how confident the neuron is
* The final MSE summarizes overall performance

Example output:

```
([0.4626, 0.4134, 0.6682], 0.3349)
```

This means:

* The neuron produced three probability predictions
* The average squared error across all predictions is 0.3349

---

## 5. Key Takeaways

* A single neuron performs a weighted sum followed by an activation function
* Sigmoid is commonly used for binary classification
* MSE helps quantify prediction accuracy
* This concept forms the foundation of neural networks and deep learning

---

## 6. Test Case:
```python
features = [[0.5, 1.0], [-1.5, -2.0], [2.0, 1.5]]
labels = [0, 1, 0]
weights = [0.7, -0.4]
bias = -0.1
result = single_neuron_model(features, labels, weights, bias)
print(result) # Expected Output: ([0.4626, 0.4134, 0.6682], 0.3349)
```
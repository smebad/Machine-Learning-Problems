# Implement ReLU Activation Function

## 1. Problem Overview

The Rectified Linear Unit (ReLU) is one of the most widely used activation functions in machine learning and deep learning. It is used inside neural networks to introduce non-linearity, which allows models to learn complex patterns.

The problem is to implement a simple Python function that applies the ReLU function to a single number. The function should return the input value if it is greater than 0; otherwise, it should return 0.

---

## 2. What Is ReLU?

The ReLU function is mathematically defined as:

ReLU(z) = max(0, z)

This means:

* If the input is positive, keep it
* If the input is zero or negative, output zero

This behavior helps neural networks avoid unnecessary negative activations and makes training faster and more stable.

---

## 3. Code With Comments

Below is your provided solution with added comments to explain each part clearly.

```python
# Define a function called relu that takes a single float input z
def relu(z: float) -> float:
    # Return the maximum of 0 and z
    # If z is positive, it returns z
    # If z is zero or negative, it returns 0
    return max(0, z)

# Test cases
if __name__ == "__main__":
    # Test with zero
    print(relu(0))    # Output: 0

    # Test with a positive number
    print(relu(1))    # Output: 1

    # Test with a negative number
    print(relu(-1))   # Output: 0
```

---

## 4. Step-by-Step Logic

1. The function receives a single number `z`.
2. The built-in `max` function compares `0` and `z`.
3. If `z` is greater than `0`, it is returned.
4. If `z` is less than or equal to `0`, `0` is returned.

This single comparison is enough to implement the full ReLU behavior.

---

## 5. How the Example Works

For the inputs:

* `relu(0)` returns `max(0, 0) = 0`
* `relu(1)` returns `max(0, 1) = 1`
* `relu(-1)` returns `max(0, -1) = 0`

So negative values are removed, while positive values pass through unchanged.

---

## 6. Alternative way to Implement ReLU

Another way to write ReLU could be using an `if` statement:

```python
def relu(z):
    if z > 0:
        return z
    else:
        return 0
```

---

## 7. Why ReLU Is Important in Machine Learning

* It makes neural networks non-linear
* It helps avoid vanishing gradients
* It is computationally efficient
* It allows deep networks to train faster

ReLU is one of the main reasons modern deep learning models work so well.

---

## 8. Key Takeaways

* ReLU keeps positive values and removes negative ones
* It is simple but extremely powerful
* The formula is just `max(0, z)`
* It is widely used in neural networks
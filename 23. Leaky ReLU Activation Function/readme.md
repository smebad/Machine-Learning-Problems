# Leaky ReLU Activation Function

## 1. Problem Overview

The Leaky ReLU activation function is a variation of the standard ReLU function used in neural networks. It helps solve a common problem of ReLU called the "dying ReLU" problem, where neurons stop learning if they always output zero for negative inputs.

The task in this problem is to implement a function that applies the Leaky ReLU formula to a given input value `z`. The function must also support a parameter `alpha` that controls how much of the negative value is allowed to pass through.

---

## 2. Mathematical Definition

The Leaky ReLU function is defined as:

If z > 0:
output = z

If z ≤ 0:
output = alpha × z

Here, `alpha` is a small positive number (usually 0.01) that allows negative inputs to produce small negative outputs instead of zero.

---

## 3. Code With Comments

```python
# Leaky ReLU implementation
def leaky_relu(z: float, alpha: float = 0.01) -> float | int:
    # If the input value is greater than 0, return it as it is
    # This keeps positive values unchanged
    if z > 0:
        return z
    
    # If the input is negative or zero, multiply it by alpha
    # This allows small negative values instead of turning them into zero
    else:
        return alpha * z
```

---

## 4. Step-by-Step Logic

1. The function receives two inputs: `z` (the value) and `alpha` (the negative slope).
2. It checks whether `z` is positive.
3. If `z` is positive, it returns `z` directly.
4. If `z` is negative or zero, it multiplies `z` by `alpha`.
5. The final result is returned.

---

## 5. Test Case Explanation

```python
print(leaky_relu(0))        # Output: 0
print(leaky_relu(1))        # Output: 1
print(leaky_relu(-1))       # Output: -0.01
print(leaky_relu(-2, 0.1))  # Output: -0.2
```

Explanation:

* `leaky_relu(0)` → 0 × alpha = 0
* `leaky_relu(1)` → positive input, returns 1
* `leaky_relu(-1)` → -1 × 0.01 = -0.01
* `leaky_relu(-2, 0.1)` → -2 × 0.1 = -0.2

---

## 6. Why Leaky ReLU is Better than ReLU

Standard ReLU works like this:

* If z > 0 → return z
* If z ≤ 0 → return 0

This can cause neurons to stop learning if they receive only negative inputs.

Leaky ReLU fixes this by allowing a small negative output instead of zero. This ensures gradients always flow and learning continues.

---

## 7. Key Takeaways

* Activation functions decide how neurons pass information forward.
* Leaky ReLU improves upon ReLU by allowing small negative values.
* The `alpha` parameter controls how much negative input is allowed.
* This helps prevent neurons from becoming inactive during training.
# Label Encoding for Ordinal Variables

## 1. What is Label Encoding for Ordinal Variables and What Problem Does It Solve?

**Label Encoding for Ordinal Variables** is a preprocessing technique used in Machine Learning to convert **ordered categorical data** into numerical form while preserving the natural ranking between categories.

Ordinal variables are categories that have a meaningful order.

Examples:

* Education level: `high school < bachelor < master < phd`
* Rating: `poor < fair < good < excellent`
* Size: `small < medium < large`

Machine learning models work with numbers, not strings. So we need to convert these categories into numbers in a way that keeps their order.

---

### The Problem It Solves

If we directly use categories like:

```
['small', 'medium', 'large']
```

A model cannot understand these strings.

If we randomly encode them like:

```
small -> 2
medium -> 0
large -> 1
```

This destroys the meaning of order.

Label Encoding for ordinal variables solves this by:

* Assigning increasing numbers based on ranking.
* Preserving the natural order in numeric form.

So the model understands:

```
small < medium < large
0     < 1      < 2
```

---

## 2. Code With Comments

```python
# Function to perform label encoding for ordinal variables
def label_encode_ordinal(values: list, order: list) -> list:
    # If the input list is empty, return an empty list
    if not values:
        return []
    
    # Create a mapping from category to its rank
    # Example: ['small', 'medium', 'large']
    # Becomes: {'small': 0, 'medium': 1, 'large': 2}
    order_map = {category: idx for idx, category in enumerate(order)}
    
    # List to store encoded results
    encoded = []
    
    # Loop through each value in input
    for val in values:
        # If value exists in the order map
        if val in order_map:
            encoded.append(order_map[val])
        else:
            # If value is unknown, encode as -1
            encoded.append(-1)
    
    return encoded

# Test Case
values = ['medium', 'small', 'large', 'small']
order = ['small', 'medium', 'large']
print(label_encode_ordinal(values, order))
```

---

## 3. Solution, Approach, and Logic

Let’s understand the approach step by step.

### Step 1: Define the Order

We are given:

```
order = ['small', 'medium', 'large']
```

This means:

| Category | Rank |
| -------- | ---- |
| small    | 0    |
| medium   | 1    |
| large    | 2    |

---

### Step 2: Create Mapping Dictionary

Using this line:

```python
order_map = {category: idx for idx, category in enumerate(order)}
```

We get:

```python
{'small': 0, 'medium': 1, 'large': 2}
```

This dictionary allows **fast lookup** of ranks.

---

### Step 3: Encode Each Value

Input:

```
values = ['medium', 'small', 'large', 'small']
```

Encoding process:

| Value  | Encoded |
| ------ | ------- |
| medium | 1       |
| small  | 0       |
| large  | 2       |
| small  | 0       |

Final Output:

```
[1, 0, 2, 0]
```

---

## Handling Unknown Categories

If input contains a value not in `order`:

Example:

```
values = ['medium', 'huge']
```

Since `huge` is not in order:

```
output = [1, -1]
```

`-1` indicates **unknown category**.

This is useful because:

* Real datasets often contain unexpected values.
* It prevents program crashes.

---

## Why Not Use Label Encoding for Nominal Data?

For **nominal variables** (like colors: red, blue, green):

There is no natural order.

If we encode:

```
red -> 0
blue -> 1
green -> 2
```

The model may think:

```
red < blue < green
```

Which is meaningless.

So label encoding is **only correct for ordinal data**.

---

## Key Takeaways

* Ordinal variables have a meaningful order.
* Label encoding converts categories into ranked numbers.
* It preserves the natural hierarchy.
* Unknown values are handled safely with -1.
* This is essential before training ML models.

---

## When to Use Label Encoding for Ordinal Variables

Use it when:

* Categories have a clear ranking.
* You want the model to learn order relationships.
* You are preparing structured tabular data.

Avoid it when:

* Categories have no order.
* You are dealing with purely nominal data.

In those cases, use **One-Hot Encoding** instead.

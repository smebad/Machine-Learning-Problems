# Label Encoding for Ordinal Variables
# Implement a function that performs label encoding on ordinal categorical variables while preserving their natural order.

# Ordinal variables are categorical variables that have a meaningful order or ranking between their categories (e.g., education level: 'high school' < 'bachelor' < 'master' < 'phd', or satisfaction rating: 'poor' < 'fair' < 'good' < 'excellent').

# Unlike nominal variables (where categories have no inherent order), ordinal variables require encoding that respects the underlying ordering relationship.

# Input:
# values: A list of categorical values (strings) to be encoded
# order: A list specifying the ordering of categories from lowest rank (will be encoded as 0) to highest rank (will be encoded as len(order)-1)
# Output:
# A list of integers where each integer represents the encoded value of the corresponding input category. If a value in values is not found in the order list, it should be encoded as -1 to indicate an unknown category.
# Constraints:
# The order list contains unique category strings
# Values in values may or may not be present in order
# If values is empty, return an empty list
# Example:
# Input:
# values = ['medium', 'small', 'large', 'small'], order = ['small', 'medium', 'large']
# Output:
# [1, 0, 2, 0]
# Reasoning:
# The order list defines: 'small' -> 0, 'medium' -> 1, 'large' -> 2. Applying this mapping: 'medium' becomes 1, 'small' becomes 0, 'large' becomes 2, 'small' becomes 0. Result: [1, 0, 2, 0].


# Solution:
def label_encode_ordinal(values: list, order: list) -> list:
    if not values:
        return []
    
    order_map = {category: idx for idx, category in enumerate(order)}
    
    encoded = []
    for val in values:
        if val in order_map:
            encoded.append(order_map[val])
        else:
            encoded.append(-1)
    
    return encoded

# Test Case
values = ['medium', 'small', 'large', 'small']
order = ['small', 'medium', 'large']
print(label_encode_ordinal(values, order))
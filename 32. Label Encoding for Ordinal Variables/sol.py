# Label Encoding for Ordinal Variables
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

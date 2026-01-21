# Implement ReLU Activation Function
# Solution:
def relu(z: float) -> float:
    return max(0, z)

# Test cases
if __name__ == "__main__":
    print(relu(0))    # Output: 0
    print(relu(1))    # Output: 1
    print(relu(-1))   # Output: 0

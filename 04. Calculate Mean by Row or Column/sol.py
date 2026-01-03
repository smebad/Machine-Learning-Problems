# Calculate Mean by Row or Column
# Write a Python function that calculates the mean of a matrix either by row or by column, based on a given mode. The function should take a matrix (list of lists) and a mode ('row' or 'column') as input and return a list of means according to the specified mode.

# Example:
# Input:
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], mode = 'column'
# Output:
# [4.0, 5.0, 6.0]
# Reasoning:
# Calculating the mean of each column results in [(1+4+7)/3, (2+5+8)/3, (3+6+9)/3].

# Solution:
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if mode == 'column':
        return [sum(col) / len(matrix) for col in zip(*matrix)]
    elif mode == 'row':
        return [sum(row) / len(row) for row in matrix]
    
# Test cases
if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    # Test for column mean
    column_mean = calculate_matrix_mean(matrix, 'column')
    print("Column Mean:", column_mean)  # Output: [4.0, 5.0, 6.0]
    
    # Test for row mean
    row_mean = calculate_matrix_mean(matrix, 'row')
    print("Row Mean:", row_mean)  # Output: [2.0, 5.0, 8.0]
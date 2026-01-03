# Calculate Mean by Row or Column
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

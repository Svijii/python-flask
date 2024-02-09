def matrix_multiply(matrix1, matrix2):
    # Check if the matrices can be multiplied
    if len(matrix1[0]) != len(matrix2):
        print("Matrix multiplication is not possible.")
        return None

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

    # Perform matrix multiplication
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

# Function to print a matrix
def print_matrix(matrix):
    for row in matrix:
        print(row)

# Example usage:
matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8], [9, 10], [11, 12]]

result_matrix = matrix_multiply(matrix1, matrix2)

if result_matrix is not None:
    print("Matrix 1:")
    print_matrix(matrix1)

    print("\nMatrix 2:")
    print_matrix(matrix2)

    print("\nResulting Matrix:")
    print_matrix(result_matrix)


# EXP47.py - Strassen's Matrix Multiplication Algorithm

def matrix_add(A, B):
    """Add two matrices"""
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C

def matrix_subtract(A, B):
    """Subtract matrix B from A"""
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]
    return C

def matrix_multiply_naive(A, B):
    """Naive matrix multiplication for base case"""
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def get_submatrix(matrix, start_row, start_col, size):
    """Extract submatrix"""
    submatrix = []
    for i in range(start_row, start_row + size):
        row = []
        for j in range(start_col, start_col + size):
            row.append(matrix[i][j])
        submatrix.append(row)
    return submatrix

def set_submatrix(matrix, submatrix, start_row, start_col):
    """Set submatrix values"""
    size = len(submatrix)
    for i in range(size):
        for j in range(size):
            matrix[start_row + i][start_col + j] = submatrix[i][j]

def strassen(A, B):
    """Strassen's Matrix Multiplication"""
    n = len(A)
    
    if n <= 2:
        return matrix_multiply_naive(A, B)
    
    size = n // 2
    
    # Extract submatrices
    A11 = get_submatrix(A, 0, 0, size)
    A12 = get_submatrix(A, 0, size, size)
    A21 = get_submatrix(A, size, 0, size)
    A22 = get_submatrix(A, size, size, size)
    
    B11 = get_submatrix(B, 0, 0, size)
    B12 = get_submatrix(B, 0, size, size)
    B21 = get_submatrix(B, size, 0, size)
    B22 = get_submatrix(B, size, size, size)
    
    # Calculate 7 products
    M1 = strassen(matrix_add(A11, A22), matrix_add(B11, B22))
    M2 = strassen(matrix_add(A21, A22), B11)
    M3 = strassen(A11, matrix_subtract(B12, B22))
    M4 = strassen(A22, matrix_subtract(B21, B11))
    M5 = strassen(matrix_add(A11, A12), B22)
    M6 = strassen(matrix_subtract(A21, A11), matrix_add(B11, B12))
    M7 = strassen(matrix_subtract(A12, A22), matrix_add(B21, B22))
    
    # Calculate result submatrices
    C11 = matrix_add(matrix_subtract(matrix_add(M1, M4), M5), M7)
    C12 = matrix_add(M3, M5)
    C21 = matrix_add(M2, M4)
    C22 = matrix_add(matrix_subtract(matrix_add(M1, M3), M2), M6)
    
    # Combine into result matrix
    C = [[0] * n for _ in range(n)]
    set_submatrix(C, C11, 0, 0)
    set_submatrix(C, C12, 0, size)
    set_submatrix(C, C21, size, 0)
    set_submatrix(C, C22, size, size)
    
    return C

def print_matrix(matrix, name="Matrix"):
    """Print matrix in readable format"""
    print(f"{name}:")
    for row in matrix:
        print(f"  {row}")

# Test Case 1
print("=" * 60)
print("Test Case 1:")
A1 = [[1, 7], [3, 5]]
B1 = [[6, 8], [4, 2]]
print("Matrix A:")
print(f"  {A1[0]}")
print(f"  {A1[1]}")
print("\nMatrix B:")
print(f"  {B1[0]}")
print(f"  {B1[1]}")
C1 = strassen(A1, B1)
print("\nMatrix C = A × B:")
print(f"  {C1[0]}")
print(f"  {C1[1]}")
print("\nExpected Output:")
print("  [34, 22]")
print("  [38, 34]")
print()

# Test Case 2
print("=" * 60)
print("Test Case 2:")
A2 = [[1, 7], [3, 5]]
B2 = [[1, 3], [7, 5]]
print("Matrix A:")
print(f"  {A2[0]}")
print(f"  {A2[1]}")
print("\nMatrix B:")
print(f"  {B2[0]}")
print(f"  {B2[1]}")
C2 = strassen(A2, B2)
print("\nMatrix C = A × B:")
print(f"  {C2[0]}")
print(f"  {C2[1]}")
print("=" * 60)

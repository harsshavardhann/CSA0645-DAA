# EXP42.py - 4Sum Problem (Count tuples summing to zero)

def count_tuples_sum_zero(A, B, C, D):
    """Count tuples (i,j,k,l) such that A[i] + B[j] + C[k] + D[l] = 0"""
    count = 0
    
    # Create dictionary for sum of pairs from C and D
    cd_sums = {}
    for c in C:
        for d in D:
            sum_cd = c + d
            cd_sums[sum_cd] = cd_sums.get(sum_cd, 0) + 1
    
    # For each pair from A and B, check if negation exists in CD sums
    for a in A:
        for b in B:
            sum_ab = a + b
            needed = -(sum_ab)  # We need CD sum = -AB sum
            
            if needed in cd_sums:
                count += cd_sums[needed]
    
    return count

# Test Case 1
print("=" * 60)
print("Test Case 1:")
A1 = [1, 2]
B1 = [-2, -1]
C1 = [-1, 2]
D1 = [0, 2]
print(f"Input: A = {A1}, B = {B1}, C = {C1}, D = {D1}")
result1 = count_tuples_sum_zero(A1, B1, C1, D1)
print(f"Output: {result1}")
print()

# Test Case 2
print("Test Case 2:")
A2 = [0]
B2 = [0]
C2 = [0]
D2 = [0]
print(f"Input: A = {A2}, B = {B2}, C = {C2}, D = {D2}")
result2 = count_tuples_sum_zero(A2, B2, C2, D2)
print(f"Output: {result2}")
print("=" * 60)

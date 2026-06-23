def find_min_max_sorted(arr):
    """Find minimum and maximum in a sorted array"""
    if len(arr) == 0:
        return None, None
    
    
    return arr[0], arr[-1]

# Test Case 1
print("=" * 50)
print("Test Case 1:")
n1 = 8
a1 = [2, 4, 6, 8, 10, 12, 14, 18]
min1, max1 = find_min_max_sorted(a1)
print(f"Input: N = {n1}, a[] = {a1}")
print(f"Output: Min = {min1}, Max = {max1}")
print()

# Test Case 2
print("Test Case 2:")
n2 = 9
a2 = [11, 13, 15, 17, 19, 21, 23, 35, 37]
min2, max2 = find_min_max_sorted(a2)
print(f"Input: N = {n2}, a[] = {a2}")
print(f"Output: Min = {min2}, Max = {max2}")
print()

# Test Case 3
print("Test Case 3:")
n3 = 10
a3 = [12, 13, 15, 17, 22, 34, 35, 36, 43, 67]
min3, max3 = find_min_max_sorted(a3)
print(f"Input: N = {n3}, a[] = {a3}")
print(f"Output: Min = {min3}, Max = {max3}")
print("=" * 50)

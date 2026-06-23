def find_min_max(arr):
    
    if len(arr) == 0:
        return None, None
    
    min_val = arr[0]
    max_val = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
        if arr[i] > max_val:
            max_val = arr[i]
    
    return min_val, max_val


print("=" * 50)
print("Test Case 1:")
n1 = 8
a1 = [5, 7, 3, 4, 9, 12, 6, 2]
min1, max1 = find_min_max(a1)
print(f"Input: N = {n1}, a[] = {a1}")
print(f"Output: Min = {min1}, Max = {max1}")
print()

print("Test Case 2:")
n2 = 9
a2 = [1, 3, 5, 7, 9, 11, 13, 15, 17]
min2, max2 = find_min_max(a2)
print(f"Input: N = {n2}, a[] = {a2}")
print(f"Output: Min = {min2}, Max = {max2}")
print()
print("Test Case 3:")
n3 = 10
a3 = [22, 34, 35, 36, 43, 67, 12, 13, 15, 17]
min3, max3 = find_min_max(a3)
print(f"Input: N = {n3}, a[] = {a3}")
print(f"Output: Min = {min3}, Max = {max3}")
print("=" * 50)

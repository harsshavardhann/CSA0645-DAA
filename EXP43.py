# EXP43.py - Median of Medians Algorithm (Find k-th smallest element)

def find_median(arr):
    """Find median of an array"""
    arr_sorted = sorted(arr)
    n = len(arr_sorted)
    if n % 2 == 1:
        return arr_sorted[n // 2]
    else:
        return (arr_sorted[n // 2 - 1] + arr_sorted[n // 2]) // 2

def partition(arr, left, right, pivot_value):
    """Partition array around pivot value"""
    # Find pivot index
    pivot_index = -1
    for i in range(left, right + 1):
        if arr[i] == pivot_value:
            pivot_index = i
            break
    
    # Move pivot to end
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    pivot_index = right
    
    store_index = left
    for i in range(left, right):
        if arr[i] < arr[pivot_index]:
            arr[i], arr[store_index] = arr[store_index], arr[i]
            store_index += 1
    
    arr[right], arr[store_index] = arr[store_index], arr[right]
    return store_index

def median_of_medians(arr, left, right, k):
    """Find k-th smallest element using median of medians"""
    if left == right:
        return arr[left]
    
    # Divide array into groups of 5
    if right - left < 5:
        sorted_arr = sorted(arr[left:right + 1])
        return sorted_arr[k - 1]
    
    medians = []
    for i in range(left, right + 1, 5):
        sub_right = min(i + 4, right)
        median = find_median(arr[i:sub_right + 1])
        medians.append(median)
    
    # Recursively find median of medians
    if len(medians) == 1:
        pivot = medians[0]
    else:
        pivot = median_of_medians(medians, 0, len(medians) - 1, len(medians) // 2 + 1)
    
    # Partition around pivot
    pivot_index = partition(arr, left, right, pivot)
    
    if k - 1 == pivot_index:
        return arr[pivot_index]
    elif k - 1 < pivot_index:
        return median_of_medians(arr, left, pivot_index - 1, k)
    else:
        return median_of_medians(arr, pivot_index + 1, right, k - pivot_index - 1)

# Test Case 1
print("=" * 60)
print("Test Case 1:")
arr1 = [12, 3, 5, 7, 19]
k1 = 2
print(f"Input: arr = {arr1}, k = {k1}")
result1 = median_of_medians(arr1[:], 0, len(arr1) - 1, k1)
print(f"Expected Output: 5")
print(f"Output: {result1}")
print()

# Test Case 2
print("Test Case 2:")
arr2 = [12, 3, 5, 7, 4, 19, 26]
k2 = 3
print(f"Input: arr = {arr2}, k = {k2}")
result2 = median_of_medians(arr2[:], 0, len(arr2) - 1, k2)
print(f"Expected Output: 5")
print(f"Output: {result2}")
print()

# Test Case 3
print("Test Case 3:")
arr3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k3 = 6
print(f"Input: arr = {arr3}, k = {k3}")
result3 = median_of_medians(arr3[:], 0, len(arr3) - 1, k3)
print(f"Expected Output: 6")
print(f"Output: {result3}")
print("=" * 60)

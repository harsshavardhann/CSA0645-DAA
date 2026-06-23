# EXP44.py - Median of Medians Function Implementation

def median_of_medians_find(arr, k):
    """
    Find k-th smallest element in unsorted array using Median of Medians algorithm
    Time Complexity: O(n) in worst case
    """
    def select(arr_copy, left, right, k_pos):
        if left == right:
            return arr_copy[left]
        
        # Base case for small arrays
        if right - left < 5:
            return sorted(arr_copy[left:right + 1])[k_pos - left]
        
        # Divide into groups of 5 and find medians
        medians = []
        for i in range(left, right + 1, 5):
            sub_right = min(i + 4, right)
            # Find median of this group
            sub_arr = sorted(arr_copy[i:sub_right + 1])
            median = sub_arr[len(sub_arr) // 2]
            medians.append(median)
        
        # Find median of medians recursively
        if len(medians) == 1:
            pivot_value = medians[0]
        else:
            pivot_value = select(medians, 0, len(medians) - 1, (len(medians) + 1) // 2)
        
        # Partition
        pivot_index = partition_helper(arr_copy, left, right, pivot_value)
        
        if k_pos == pivot_index + 1:
            return arr_copy[pivot_index]
        elif k_pos <= pivot_index:
            return select(arr_copy, left, pivot_index - 1, k_pos)
        else:
            return select(arr_copy, pivot_index + 1, right, k_pos)
    
    def partition_helper(arr_copy, left, right, pivot_val):
        idx = left
        for i in range(left, right + 1):
            if arr_copy[i] == pivot_val:
                idx = i
                break
        arr_copy[idx], arr_copy[right] = arr_copy[right], arr_copy[idx]
        
        store_idx = left
        for i in range(left, right):
            if arr_copy[i] < arr_copy[right]:
                arr_copy[i], arr_copy[store_idx] = arr_copy[store_idx], arr_copy[i]
                store_idx += 1
        arr_copy[right], arr_copy[store_idx] = arr_copy[store_idx], arr_copy[right]
        return store_idx
    
    arr_copy = arr[:]
    return select(arr_copy, 0, len(arr_copy) - 1, k)

# Test Case 1
print("=" * 70)
print("Test Case 1:")
arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k1 = 6
print(f"Input: arr = {arr1}, k = {k1}")
result1 = median_of_medians_find(arr1, k1)
print(f"Output: The {k1}-th smallest element is {result1}")
print()

# Test Case 2
print("Test Case 2:")
arr2 = [23, 17, 31, 44, 55, 21, 20, 18, 19, 27]
k2 = 5
print(f"Input: arr = {arr2}, k = {k2}")
result2 = median_of_medians_find(arr2, k2)
print(f"Output: The {k2}-th smallest element is {result2}")
print()

# Verify with sorted array
print("Verification:")
sorted_arr2 = sorted(arr2)
print(f"Sorted array: {sorted_arr2}")
print(f"5th smallest element (index 4) = {sorted_arr2[4]}")
print("=" * 70)

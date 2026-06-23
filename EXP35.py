# EXP35.py - Merge Sort Algorithm

def merge(arr, left, mid, right):
    """Merge two sorted subarrays"""
    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]
    
    i = j = 0
    k = left
    
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    """Merge Sort implementation"""
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

# Test Case 1
print("=" * 50)
print("Test Case 1:")
n1 = 8
a1 = [31, 23, 35, 27, 11, 21, 15, 28]
print(f"Input: N = {n1}, a[] = {a1}")
merge_sort(a1, 0, len(a1) - 1)
print(f"Output: {','.join(map(str, a1))}")
print()

# Test Case 2
print("Test Case 2:")
n2 = 10
a2 = [22, 34, 25, 36, 43, 67, 52, 13, 65, 17]
print(f"Input: N = {n2}, a[] = {a2}")
merge_sort(a2, 0, len(a2) - 1)
print(f"Output: {','.join(map(str, a2))}")
print("=" * 50)

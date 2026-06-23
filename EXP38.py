# EXP38.py - Quick Sort (Middle Element as Pivot)

def partition_middle(arr, low, high, steps):
    """Partition using middle element as pivot"""
    mid = (low + high) // 2
    arr[low], arr[mid] = arr[mid], arr[low]
    
    pivot = arr[low]
    i = low + 1
    
    while i <= high:
        if arr[i] < pivot:
            arr[low], arr[i] = arr[i], arr[low]
            low = i
        i += 1
    
    arr[low] = pivot
    pivot_index = low
    steps.append(f"Partition around {pivot}: {arr[:]}")
    return pivot_index

def quick_sort_middle(arr, low, high, steps):
    """Quick Sort using middle element as pivot"""
    if low < high:
        pi = partition_middle(arr, low, high, steps)
        quick_sort_middle(arr, low, pi - 1, steps)
        quick_sort_middle(arr, pi + 1, high, steps)

def quick_sort_middle_with_steps(arr):
    """Quick Sort with middle pivot and step tracking"""
    steps = []
    steps.append(f"Initial array: {arr[:]}")
    quick_sort_middle(arr, 0, len(arr) - 1, steps)
    return arr, steps

# Test Case 1
print("=" * 50)
print("Test Case 1:")
n1 = 8
a1 = [19, 72, 35, 46, 58, 91, 22, 31]
print(f"Input: N = {n1}, a[] = {a1}")
sorted_a1, steps1 = quick_sort_middle_with_steps(a1[:])
print("Steps during sorting:")
for step in steps1:
    print(f"  {step}")
print(f"Output: {','.join(map(str, sorted_a1))}")
print()

# Test Case 2
print("Test Case 2:")
n2 = 8
a2 = [31, 23, 35, 27, 11, 21, 15, 28]
print(f"Input: N = {n2}, a[] = {a2}")
sorted_a2, steps2 = quick_sort_middle_with_steps(a2[:])
print(f"Output: {','.join(map(str, sorted_a2))}")
print()

# Test Case 3
print("Test Case 3:")
n3 = 10
a3 = [22, 34, 25, 36, 43, 67, 52, 13, 65, 17]
print(f"Input: N = {n3}, a[] = {a3}")
sorted_a3, steps3 = quick_sort_middle_with_steps(a3[:])
print(f"Output: {','.join(map(str, sorted_a3))}")
print("=" * 50)

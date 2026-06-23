# EXP37.py - Quick Sort (First Element as Pivot)

def partition_first(arr, low, high, steps):
    """Partition using first element as pivot"""
    pivot = arr[low]
    i = low + 1
    
    while i <= high:
        if arr[i] < pivot:
            arr[low], arr[i] = arr[i], arr[low]
            low = i
        i += 1
    
    arr[low] = pivot
    pivot_index = low
    steps.append(f"After partition: {arr[:]}")
    return pivot_index

def quick_sort_first(arr, low, high, steps):
    """Quick Sort using first element as pivot"""
    if low < high:
        pi = partition_first(arr, low, high, steps)
        quick_sort_first(arr, low, pi - 1, steps)
        quick_sort_first(arr, pi + 1, high, steps)

def quick_sort_with_steps(arr):
    """Quick Sort with step tracking"""
    steps = []
    steps.append(f"Initial array: {arr[:]}")
    quick_sort_first(arr, 0, len(arr) - 1, steps)
    return arr, steps

# Test Case 1
print("=" * 50)
print("Test Case 1:")
n1 = 9
a1 = [10, 16, 8, 12, 15, 6, 3, 9, 5]
print(f"Input: N = {n1}, a[] = {a1}")
sorted_a1, steps1 = quick_sort_with_steps(a1[:])
print("Steps during sorting:")
for step in steps1:
    print(f"  {step}")
print(f"Output: {','.join(map(str, sorted_a1))}")
print()

# Test Case 2
print("Test Case 2:")
n2 = 8
a2 = [12, 4, 78, 23, 45, 67, 89, 1]
print(f"Input: N = {n2}, a[] = {a2}")
sorted_a2, steps2 = quick_sort_with_steps(a2[:])
print(f"Output: {','.join(map(str, sorted_a2))}")
print()

# Test Case 3
print("Test Case 3:")
n3 = 7
a3 = [38, 27, 43, 3, 9, 82, 10]
print(f"Input: N = {n3}, a[] = {a3}")
sorted_a3, steps3 = quick_sort_with_steps(a3[:])
print(f"Output: {','.join(map(str, sorted_a3))}")
print("=" * 50)

# EXP40.py - Binary Search with Step-by-Step Explanation

def binary_search_steps(arr, target):
    """Binary search with step-by-step midpoint calculations"""
    left = 0
    right = len(arr) - 1
    steps = []
    
    steps.append(f"Searching for {target} in array: {arr}")
    steps.append("")
    
    iteration = 1
    while left <= right:
        mid = (left + right) // 2
        steps.append(f"Iteration {iteration}:")
        steps.append(f"  left = {left}, right = {right}, mid = {mid}")
        steps.append(f"  arr[mid] = {arr[mid]}")
        
        if arr[mid] == target:
            steps.append(f"  Found! Position = {mid + 1} (1-indexed)")
            return mid + 1, steps
        elif arr[mid] < target:
            steps.append(f"  {arr[mid]} < {target}, move left pointer")
            left = mid + 1
        else:
            steps.append(f"  {arr[mid]} > {target}, move right pointer")
            right = mid - 1
        
        steps.append("")
        iteration += 1
    
    steps.append(f"Element not found!")
    return -1, steps

# Test Case 1
print("=" * 70)
print("Test Case 1: Sorted Array")
n1 = 9
a1 = [3, 9, 14, 19, 25, 31, 42, 47, 53]
search_key1 = 31
print(f"Input: N = {n1}, a[] = {a1}, search key = {search_key1}")
print()
result1, steps1 = binary_search_steps(a1, search_key1)
for step in steps1:
    print(step)
print(f"Output: Position = {result1}")
print()

# Test Case 2
print("=" * 70)
print("Test Case 2:")
n2 = 7
a2 = [13, 19, 24, 29, 35, 41, 42]
search_key2 = 42
print(f"Input: N = {n2}, a[] = {a2}, search key = {search_key2}")
print()
result2, steps2 = binary_search_steps(a2, search_key2)
for step in steps2:
    print(step)
print(f"Output: Position = {result2}")
print()

# Test Case 3
print("=" * 70)
print("Test Case 3:")
n3 = 6
a3 = [20, 40, 60, 80, 100, 120]
search_key3 = 60
print(f"Input: N = {n3}, a[] = {a3}, search key = {search_key3}")
print()
result3, steps3 = binary_search_steps(a3, search_key3)
for step in steps3:
    print(step)
print(f"Output: Position = {result3}")
print()

print("=" * 70)
print("Note: Binary Search requires the array to be SORTED for correct results.")
print("If the array is unsorted, the algorithm may not find elements correctly,")
print("or may return incorrect positions, compromising both correctness and performance.")
print("=" * 70)

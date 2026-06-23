# EXP46.py - Meet in the Middle Technique (Exact Sum Subset)

def subset_sum_exact(arr, exact_sum):
    """
    Determine if there exists a subset with exact sum using Meet in the Middle
    Time Complexity: O(2^(n/2)) instead of O(2^n)
    """
    n = len(arr)
    mid = n // 2
    
    # First half subset sums
    first_half_sums = set()
    for i in range(1 << mid):
        sum_val = 0
        for j in range(mid):
            if i & (1 << j):
                sum_val += arr[j]
        first_half_sums.add(sum_val)
    
    # Second half subset sums and check against first half
    for i in range(1 << (n - mid)):
        sum_val = 0
        for j in range(n - mid):
            if i & (1 << j):
                sum_val += arr[mid + j]
        
        # Check if complement exists in first half
        complement = exact_sum - sum_val
        if complement in first_half_sums:
            return True
    
    return False

def find_subset_with_sum(arr, exact_sum):
    """Find actual subset with exact sum"""
    n = len(arr)
    mid = n // 2
    
    # Store first half subsets
    first_half_subsets = {}
    for i in range(1 << mid):
        sum_val = 0
        subset = []
        for j in range(mid):
            if i & (1 << j):
                sum_val += arr[j]
                subset.append(arr[j])
        if sum_val not in first_half_subsets:
            first_half_subsets[sum_val] = subset
    
    # Check second half and find matching subset
    for i in range(1 << (n - mid)):
        sum_val = 0
        subset2 = []
        for j in range(n - mid):
            if i & (1 << j):
                sum_val += arr[mid + j]
                subset2.append(arr[mid + j])
        
        complement = exact_sum - sum_val
        if complement in first_half_subsets:
            return first_half_subsets[complement] + subset2
    
    return None

# Test Case 1
print("=" * 70)
print("Test Case 1:")
arr1 = [1, 3, 9, 2, 7, 12]
target1 = 15
print(f"Array E = {arr1}")
print(f"Exact Sum = {target1}")
result1 = subset_sum_exact(arr1, target1)
subset1 = find_subset_with_sum(arr1, target1)
print(f"Output: {result1}")
if subset1:
    print(f"Subset found: {subset1}")
    print(f"Sum: {sum(subset1)}")
print()

# Test Case 2
print("Test Case 2:")
arr2 = [3, 34, 4, 12, 5, 2]
target2 = 15
print(f"Array E = {arr2}")
print(f"Exact Sum = {target2}")
result2 = subset_sum_exact(arr2, target2)
subset2 = find_subset_with_sum(arr2, target2)
print(f"Output: {result2}")
if subset2:
    print(f"Subset found: {subset2}")
    print(f"Sum: {sum(subset2)}")
print("=" * 70)

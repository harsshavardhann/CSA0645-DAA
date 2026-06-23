# EXP45.py - Meet in the Middle Technique (Closest to Target Sum)

def closest_subset_sum(arr, target):
    """
    Find subset whose sum is closest to target using Meet in the Middle technique
    """
    n = len(arr)
    mid = n // 2
    
    # First half subsets and their sums
    first_half_sums = {}
    for i in range(1 << (mid)):
        sum_val = 0
        subset = []
        for j in range(mid):
            if i & (1 << j):
                sum_val += arr[j]
                subset.append(arr[j])
        if sum_val not in first_half_sums:
            first_half_sums[sum_val] = []
        first_half_sums[sum_val].append(subset)
    
    # Second half subsets and their sums
    second_half_sums = {}
    for i in range(1 << (n - mid)):
        sum_val = 0
        subset = []
        for j in range(n - mid):
            if i & (1 << j):
                sum_val += arr[mid + j]
                subset.append(arr[mid + j])
        if sum_val not in second_half_sums:
            second_half_sums[sum_val] = []
        second_half_sums[sum_val].append(subset)
    
    # Find closest sum
    closest_diff = float('inf')
    best_subset = []
    best_sum = 0
    
    for sum1 in first_half_sums:
        for sum2 in second_half_sums:
            total_sum = sum1 + sum2
            diff = abs(total_sum - target)
            
            if diff < closest_diff:
                closest_diff = diff
                best_sum = total_sum
                best_subset = first_half_sums[sum1][0] + second_half_sums[sum2][0]
    
    return best_subset, best_sum, target

# Test Case 1
print("=" * 70)
print("Test Case 1:")
set1 = [45, 34, 4, 12, 5, 2]
target1 = 42
print(f"Set[] = {set1}")
print(f"Target Sum: {target1}")
subset1, sum1, tgt1 = closest_subset_sum(set1, target1)
print(f"Closest subset: {subset1}")
print(f"Subset sum: {sum1}")
print(f"Difference from target: {abs(sum1 - target1)}")
print()

# Test Case 2
print("Test Case 2:")
set2 = [1, 3, 2, 7, 4, 6]
target2 = 10
print(f"Set[] = {set2}")
print(f"Target Sum: {target2}")
subset2, sum2, tgt2 = closest_subset_sum(set2, target2)
print(f"Closest subset: {subset2}")
print(f"Subset sum: {sum2}")
print(f"Difference from target: {abs(sum2 - target2)}")
print("=" * 70)

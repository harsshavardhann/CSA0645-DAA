def countPairs(nums, k):
    n = len(nums)
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j] and (i * j) % k == 0:
                count += 1

    return count


# Example 1
nums = [3, 1, 2, 2, 2, 1, 3]
k = 2
print(countPairs(nums, k))

# Example 2
nums = [1, 2, 3, 4]
k = 1
print(countPairs(nums, k))

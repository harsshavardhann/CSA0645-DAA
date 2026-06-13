def sumCounts(nums):
    n = len(nums)
    total = 0

    for i in range(n):
        distinct = set()

        for j in range(i, n):
            distinct.add(nums[j])
            count = len(distinct)
            total += count * count

    return total


# Example 1
nums = [1, 2, 1]
print(sumCounts(nums))

# Example 2
nums = [1, 1]
print(sumCounts(nums))

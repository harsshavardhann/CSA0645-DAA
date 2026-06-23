def findPeakElement(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left


# Example 1
nums1 = [1, 2, 3, 1]
print("Peak Index:", findPeakElement(nums1))

# Example 2
nums2 = [1, 2, 1, 3, 5, 6, 4]
print("Peak Index:", findPeakElement(nums2))

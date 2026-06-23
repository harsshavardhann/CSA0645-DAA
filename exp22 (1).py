def findKthPositive(arr, k):
    current = 1
    i = 0

    while k > 0:
        # If current number is missing
        if i >= len(arr) or arr[i] != current:
            k -= 1
            if k == 0:
                return current
        else:
            i += 1

        current += 1

# Example 1
arr = [2, 3, 4, 7, 11]
k = 5
print(findKthPositive(arr, k))  # Output: 9

# Example 2
arr = [1, 2, 3, 4]
k = 2
print(findKthPositive(arr, k))  # Output: 6

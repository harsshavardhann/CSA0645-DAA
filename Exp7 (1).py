def unique_elements(arr):
    unique = []
    seen = set()

    for num in arr:
        if num not in seen:
            unique.append(num)
            seen.add(num)

    return unique

# Test Cases
print(unique_elements([3, 7, 3, 5, 2, 5, 9, 2]))
print(unique_elements([-1, 2, -1, 3, 2, -2]))
print(unique_elements([1000000, 999999, 1000000]))

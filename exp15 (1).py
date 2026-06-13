def largeGroupPositions(s):
    result = []
    start = 0

    for i in range(1, len(s) + 1):
        if i == len(s) or s[i] != s[start]:
            if i - start >= 3:
                result.append([start, i - 1])
            start = i

    return result


# Example 1
s = "abbxxxxzzy"
print(largeGroupPositions(s))   # Output: [[3, 6]]

# Example 2
s = "abc"
print(largeGroupPositions(s))   # Output: []

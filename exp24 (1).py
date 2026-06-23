def strStr(haystack, needle):
    n = len(haystack)
    m = len(needle)

    for i in range(n - m + 1):
        if haystack[i:i + m] == needle:
            return i

    return -1


# Example 1
haystack = "sadbutsad"
needle = "sad"
print(strStr(haystack, needle))  # Output: 0

# Example 2
haystack = "leetcode"
needle = "leeto"
print(strStr(haystack, needle))  # Output: -1

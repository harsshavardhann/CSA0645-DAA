def find_max_after_sort(arr):
    if not arr:
        return "List is empty"

    arr.sort()  # Efficient sorting: O(n log n)
    return arr[-1]

# Test Cases
print(find_max_after_sort([]))
print(find_max_after_sort([5]))
print(find_max_after_sort([3, 3, 3, 3, 3]))

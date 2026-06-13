def binary_search(arr, key):
    arr.sort()  # Binary search requires sorted array

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid + 1  # Position starting from 1

        elif arr[mid] < key:
            low = mid + 1

        else:
            high = mid - 1

    return -1

# Test Cases
arr = [3, 4, 6, -9, 10, 8, 9, 30]

key = 10
result = binary_search(arr, key)
if result != -1:
    print(f"Element {key} is found at position {result}")
else:
    print(f"Element {key} is not found")

key = 100
result = binary_search(arr, key)
if result != -1:
    print(f"Element {key} is found at position {result}")
else:
    print(f"Element {key} is not found")

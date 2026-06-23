def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Stop early if no swaps occurred
        if not swapped:
            break

    return arr

# Example
numbers = [1, 2, 3, 4, 5]
print("Original List:", numbers)
print("Sorted List:", bubble_sort(numbers))

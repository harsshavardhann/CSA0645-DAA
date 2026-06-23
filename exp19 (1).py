# Selection Sort in Python

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        # Find the smallest element in the unsorted part
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# Example 1: Random Array
arr1 = [5, 2, 9, 1, 5, 6]
print("Input:", arr1)
print("Sorted:", selection_sort(arr1.copy()))

# Example 2: Reverse Sorted Array
arr2 = [10, 8, 6, 4, 2]
print("\nInput:", arr2)
print("Sorted:", selection_sort(arr2.copy()))

# Example 3: Already Sorted Array
arr3 = [1, 2, 3, 4, 5]
print("\nInput:", arr3)
print("Sorted:", selection_sort(arr3.copy()))

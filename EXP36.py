
class MergeSortCounter:
    def __init__(self):
        self.comparison_count = 0
    
    def merge(self, arr, left, mid, right):
        """Merge two sorted subarrays and count comparisons"""
        left_arr = arr[left:mid + 1]
        right_arr = arr[mid + 1:right + 1]
        
        i = j = 0
        k = left
        
        while i < len(left_arr) and j < len(right_arr):
            self.comparison_count += 1
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
    
    def merge_sort(self, arr, left, right):
        """Merge Sort with comparison counting"""
        if left < right:
            mid = (left + right) // 2
            self.merge_sort(arr, left, mid)
            self.merge_sort(arr, mid + 1, right)
            self.merge(arr, left, mid, right)
    
    def sort(self, arr):
        """Main sort function that returns sorted array and comparison count"""
        self.merge_sort(arr, 0, len(arr) - 1)
        return arr, self.comparison_count

# Test Case 1
print("=" * 50)
print("Test Case 1:")
n1 = 8
a1 = [12, 4, 78, 23, 45, 67, 89, 1]
print(f"Input: N = {n1}, a[] = {a1}")
counter1 = MergeSortCounter()
sorted_a1, comparisons1 = counter1.sort(a1)
print(f"Sorted Array: {','.join(map(str, sorted_a1))}")
print(f"Number of Comparisons: {comparisons1}")
print()

# Test Case 2
print("Test Case 2:")
n2 = 7
a2 = [38, 27, 43, 3, 9, 82, 10]
print(f"Input: N = {n2}, a[] = {a2}")
counter2 = MergeSortCounter()
sorted_a2, comparisons2 = counter2.sort(a2)
print(f"Sorted Array: {','.join(map(str, sorted_a2))}")
print(f"Number of Comparisons: {comparisons2}")
print("=" * 50)

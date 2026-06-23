class BinarySearchCounter:
    def __init__(self):
        self.comparison_count = 0
    
    def binary_search(self, arr, target):
        """Binary search with comparison counting"""
        left = 0
        right = len(arr) - 1
        
        while left <= right:
            self.comparison_count += 1
            mid = (left + right) // 2
            
            if arr[mid] == target:
                return mid + 1  # 1-indexed position
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1  # Element not found

# Test Case 1
print("=" * 50)
print("Test Case 1:")
n1 = 9
a1 = [5, 10, 15, 20, 25, 30, 35, 40, 45]
search_key1 = 20
print(f"Input: N = {n1}, a[] = {a1}, search key = {search_key1}")
bs1 = BinarySearchCounter()
result1 = bs1.binary_search(a1, search_key1)
print(f"Output: Position = {result1}")
print(f"Number of Comparisons: {bs1.comparison_count}")
print()

# Test Case 2
print("Test Case 2:")
n2 = 6
a2 = [10, 20, 30, 40, 50, 60]
search_key2 = 50
print(f"Input: N = {n2}, a[] = {a2}, search key = {search_key2}")
bs2 = BinarySearchCounter()
result2 = bs2.binary_search(a2, search_key2)
print(f"Output: Position = {result2}")
print(f"Number of Comparisons: {bs2.comparison_count}")
print()

print("Test Case 3:")
n3 = 7
a3 = [21, 32, 40, 54, 65, 76, 87]
search_key3 = 32
print(f"Input: N = {n3}, a[] = {a3}, search key = {search_key3}")
bs3 = BinarySearchCounter()
result3 = bs3.binary_search(a3, search_key3)
print(f"Output: Position = {result3}")
print(f"Number of Comparisons: {bs3.comparison_count}")
print("=" * 50)

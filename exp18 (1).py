# Function to sort a list
def sort_list(arr):
    arr.sort()
    return arr

# Input
n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    arr.append(int(input()))

# Output
print("Sorted List:", sort_list(arr))

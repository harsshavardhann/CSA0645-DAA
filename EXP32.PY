import itertools

def total_value(items, values):
    """Sum values of selected items by indices"""
    return sum(values[i] for i in items)

def is_feasible(items, weights, capacity):
    """Check if total weight <= capacity"""
    return sum(weights[i] for i in items) <= capacity

def knapsack_exhaustive(weights, values, capacity):
    """
    Exhaustive 0-1 knapsack: checks all subsets
    Returns: best_items, max_value
    """
    n = len(weights)
    max_val = 0
    best_items = []

    # Generate all subsets using combinations of all lengths
    for r in range(n + 1):
        for combo in itertools.combinations(range(n), r):
            if is_feasible(combo, weights, capacity):
                val = total_value(combo, values)
                if val > max_val:
                    max_val = val
                    best_items = list(combo)

    return best_items, max_val

# Test Case 1
weights1 = [2, 3, 1]
values1 = [4, 5, 3]
capacity1 = 4
items1, val1 = knapsack_exhaustive(weights1, values1, capacity1)
print("Test Case 1:")
print(f"Optimal Selection: {items1} (Items with indices {', '.join(map(str, items1))})")
print(f"Total Value: {val1}")

print()

# Test Case 2
weights2 = [1, 2, 3, 4]
values2 = [2, 4, 6, 3]
capacity2 = 6
items2, val2 = knapsack_exhaustive(weights2, values2, capacity2)
print("Test Case 2:")
print(f"Optimal Selection: {items2} (Items with indices {', '.join(map(str, items2))})")
print(f"Total Value: {val2}")
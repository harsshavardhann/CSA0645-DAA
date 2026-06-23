import itertools

def total_cost(assignment, cost_matrix):
    """Calculate total cost for a given assignment"""
    return sum(cost_matrix[worker][task] for worker, task in enumerate(assignment))

def assignment_problem(cost_matrix):
    """
    Exhaustive search for assignment problem
    assignment[i] = j means worker i assigned to task j
    """
    n = len(cost_matrix)
    min_cost = float('inf')
    best_assignment = None

    # Generate all permutations of task indices
    for perm in itertools.permutations(range(n)):
        cost = total_cost(perm, cost_matrix)
        if cost < min_cost:
            min_cost = cost
            best_assignment = perm

    # Format output as [(worker 1, task x),...]
    result = [(f"worker {i+1}", f"task {best_assignment[i]+1}") for i in range(n)]
    return result, min_cost

# Test Case 1
cost1 = [
    [3, 10, 7],
    [8, 5, 12],
    [4, 6, 9]
]
assign1, cost1_total = assignment_problem(cost1)
print("Test Case 1:")
print("Optimal Assignment:", assign1)
print("Total Cost:", cost1_total)

print()

# Test Case 2
cost2 = [
    [15, 9, 4],
    [8, 7, 18],
    [6, 12, 11]
]
assign2, cost2_total = assignment_problem(cost2)
print("Test Case 2:")
print("Optimal Assignment:", assign2)
print("Total Cost:", cost2_total)
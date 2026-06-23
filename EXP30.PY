import itertools
import math

def distance(city1, city2):
    """Euclidean distance between two cities"""
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def tsp(cities):
    """
    Exhaustive TSP: tries all permutations of cities[1:]
    Returns: min_distance, shortest_path
    """
    if len(cities) < 2:
        return 0, cities

    start = cities[0]
    min_dist = float('inf')
    best_path = []

    # Generate all permutations of remaining cities
    for perm in itertools.permutations(cities[1:]):
        # Build full path: start -> perm -> start
        path = [start] + list(perm) + [start]

        # Calculate total distance for this route
        total = 0
        for i in range(len(path) - 1):
            total += distance(path[i], path[i + 1])

        # Track shortest
        if total < min_dist:
            min_dist = total
            best_path = path

    return min_dist, best_path

# Test Case 1: Four cities
cities1 = [(1, 2), (4, 5), (7, 1), (3, 6)]
dist1, path1 = tsp(cities1)
print("Test Case 1:")
print(f"Shortest Distance: {dist1}")
print(f"Shortest Path: {path1}")

print()

# Test Case 2: Five cities
cities2 = [(2, 4), (8, 1), (1, 7), (6, 3), (5, 9)]
dist2, path2 = tsp(cities2)
print("Test Case 2:")
print(f"Shortest Distance: {dist2}")
print(f"Shortest Path: {path2}")
# EXP41.py - K Closest Points to Origin

import math

def distance_from_origin(point):
    """Calculate squared distance from origin (0, 0)"""
    return point[0] ** 2 + point[1] ** 2

def k_closest_points(points, k):
    """Find k closest points to origin (0, 0)"""
    # Create list of (distance, point) pairs
    distances = []
    for point in points:
        dist = distance_from_origin(point)
        distances.append((dist, point))
    
    # Sort by distance
    distances.sort(key=lambda x: x[0])
    
    # Extract k closest points
    result = [point for dist, point in distances[:k]]
    return result

# Test Case 1
print("=" * 60)
print("Test Case 1:")
points1 = [[1, 3], [-2, 2], [5, 8], [0, 1]]
k1 = 2
print(f"Input: points = {points1}, k = {k1}")
result1 = k_closest_points(points1, k1)
print(f"Output: {result1}")
print()

# Test Case 2
print("Test Case 2:")
points2 = [[1, 3], [-2, 2]]
k2 = 1
print(f"Input: points = {points2}, k = {k2}")
result2 = k_closest_points(points2, k2)
print(f"Output: {result2}")
print()

# Test Case 3
print("Test Case 3:")
points3 = [[3, 3], [5, -1], [-2, 4]]
k3 = 2
print(f"Input: points = {points3}, k = {k3}")
result3 = k_closest_points(points3, k3)
print(f"Output: {result3}")
print("=" * 60)

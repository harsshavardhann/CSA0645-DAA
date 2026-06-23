import math
def dist(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def closest_pair_brute(points):
    min_d = float('inf')
    pair = None
    n = len(points)
    for i in range(n):
        for j in range(i+1, n):
            d = dist(points[i], points[j])
            if d < min_d:
                min_d = d
                pair = (points[i], points[j])
    return pair, min_d

points = [(1, 2), (4, 5), (7, 8), (3, 1)]
print(closest_pair_brute(points)) 
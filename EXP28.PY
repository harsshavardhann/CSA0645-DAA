import math

# ---------- Closest Pair of Points - Brute Force ----------

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def closest_pair_brute_force(points):
    n = len(points)
    if n < 2:
        return None, float('inf')

    min_dist = float('inf')
    closest_pair = (None, None)

    for i in range(n):
        for j in range(i + 1, n):
            d = euclidean_distance(points[i], points[j])
            if d < min_dist:
                min_dist = d
                closest_pair = (points[i], points[j])

    return closest_pair, min_dist

# ---------- Convex Hull - Brute Force with Colinear ----------

def orientation(p, q, r):
    # 0 -> colinear, 1 -> clockwise, 2 -> counterclockwise
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2

def on_segment(p, q, r):
    # Check if point q lies on segment pr
    return (min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and
            min(p[1], r[1]) <= q[1] <= max(p[1], r[1]))

def convex_hull_brute_force(points):
    n = len(points)
    if n < 3:
        return points

    hull_set = set()

    for i in range(n):
        for j in range(i + 1, n):
            p, q = points[i], points[j]
            valid = True
            side = None
            colinear_points = []

            for k in range(n):
                if k == i or k == j:
                    continue
                o = orientation(p, q, points[k])

                if o == 0: # colinear
                    if on_segment(p, points[k], q):
                        colinear_points.append(points[k])
                else:
                    if side is None:
                        side = o
                    elif o!= side:
                        valid = False
                        break

            if valid:
                hull_set.add(p)
                hull_set.add(q)
                for cp in colinear_points:
                    hull_set.add(cp)

    # Sort hull points in counter-clockwise order
    hull = list(hull_set)
    if not hull:
        return hull
    cx = sum(p[0] for p in hull) / len(hull)
    cy = sum(p[1] for p in hull) / len(hull)
    hull.sort(key=lambda p: math.atan2(p[1] - cy, p[0] - cx))
    return hull

# ---------- Test Both ----------

if __name__ == "__main__":
    print("=== Closest Pair Brute Force ===")
    points1 = [(1, 2), (4, 5), (7, 8), (3, 1)]
    pair, dist = closest_pair_brute_force(points1)
    print(f"Points: {points1}")
    print(f"Closest pair: {pair[0]} - {pair[1]}")
    print(f"Minimum distance: {dist}") # Time: O(n^2)
    print()

    print("=== Convex Hull Brute Force ===")
    S = [(10,0), (11,5), (5,3), (9,3.5), (15,3), (12.5,7), (6,6.5), (7.5,4.5)]
    print(f"Input points: P1(10,0), P2(11,5), P3(5,3), P4(9,3.5), P5(15,3), P6(12.5,7), P7(6,6.5), P8(7.5,4.5)")
    hull = convex_hull_brute_force(S)
    print("Convex Hull:", hull) # Time: O(n^3)

    # Map back to P1..P8 labels
    labels = {(10,0): 'P1', (11,5): 'P2', (5,3): 'P3', (9,3.5): 'P4',
              (15,3): 'P5', (12.5,7): 'P6', (6,6.5): 'P7', (7.5,4.5): 'P8'}
    print("Hull points:", [labels[p] for p in hull])
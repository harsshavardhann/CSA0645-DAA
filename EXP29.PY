import math

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

    # Check each pair of points
    for i in range(n):
        for j in range(i + 1, n):
            p, q = points[i], points[j]
            valid = True
            side = None

            for k in range(n):
                if k == i or k == j:
                    continue
                o = orientation(p, q, points[k])

                if o == 0: # colinear
                    if on_segment(p, points[k], q):
                        hull_set.add(points[k])
                else:
                    if side is None:
                        side = o
                    elif o!= side:
                        valid = False
                        break

            if valid:
                hull_set.add(p)
                hull_set.add(q)

    # Sort hull points in counter-clockwise order
    hull = list(hull_set)
    if len(hull) <= 1:
        return hull

    cx = sum(p[0] for p in hull) / len(hull)
    cy = sum(p[1] for p in hull) / len(hull)
    hull.sort(key=lambda p: math.atan2(p[1] - cy, p[0] - cx))
    return hull

# Test with given input
points = [(1, 1), (4, 6), (8, 1), (0, 0), (3, 3)]
result = convex_hull_brute_force(points)
print("Convex Hull:", result)
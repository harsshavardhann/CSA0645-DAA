def champagneTower(poured, query_row, query_glass):
    tower = [[0.0] * (r + 1) for r in range(101)]
    tower[0][0] = poured

    for r in range(query_row + 1):
        for c in range(r + 1):
            overflow = max(0, tower[r][c] - 1)

            if overflow > 0:
                tower[r + 1][c] += overflow / 2
                tower[r + 1][c + 1] += overflow / 2

    return min(1, tower[query_row][query_glass])


# Input
poured = int(input("Enter poured cups: "))
query_row = int(input("Enter query row: "))
query_glass = int(input("Enter query glass: "))

# Output
print(f"{champagneTower(poured, query_row, query_glass):.5f}")

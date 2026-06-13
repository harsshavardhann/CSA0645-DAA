def gameOfLife(board):
    m = len(board)
    n = len(board[0])

    directions = [(-1,-1), (-1,0), (-1,1),
                  (0,-1),         (0,1),
                  (1,-1),  (1,0), (1,1)]

    new_board = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            live_neighbors = 0

            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n:
                    live_neighbors += board[ni][nj]

            if board[i][j] == 1:
                if live_neighbors == 2 or live_neighbors == 3:
                    new_board[i][j] = 1
            else:
                if live_neighbors == 3:
                    new_board[i][j] = 1

    return new_board


# Input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

board = []
print("Enter the board row by row:")
for _ in range(rows):
    row = list(map(int, input().split()))
    board.append(row)

# Output
print("Next State:")
for row in gameOfLife(board):
    print(row)

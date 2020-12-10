n, m = [int(x) for x in input().split()]
board = [["" for x in range(n)] for x in range(n)]
for u in range(m):
    a, b = [int(x) for x in input().split()]
    board[a-1][b-1] = "q"
    #horizontal
    for x in range(n):
        if board[a-1][x] == "":
            board[a-1][x] = "h"
    #vertical
    for x in range(n):
        if board[x][b-1] == "":
            board[x][b-1] = "v"
    #diagonal
    c = a-1
    d = b-1
    for x in range(n):
        if c >= 0 and d >= 0:
            if board[c][d] == "":
                board[c][d] = "d"
            c -= 1
            d -= 1
    c = a-1
    d = b-1
    for x in range(n):
        if c <= n-1 and d <= n-1:
            if board[c][d] == "":
                board[c][d] = "d"
            c += 1
            d += 1
    c = a-1
    d = b-1
    for x in range(n):
        if c >= 0 and d <= n-1:
            if board[c][d] == "":
                board[c][d] = "d"
            c -= 1
            d += 1
    c = a-1
    d = b-1
    for x in range(n):
        if c <= n-1 and d >= 0:
            if board[c][d] == "":
                board[c][d] = "d"
            c += 1
            d -= 1
empty = 0
for x in range(n):
    for y in range(n):
        if board[x][y] == "":
            empty += 1
print(empty)
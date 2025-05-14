def count_recolor_point(x, y, board) -> int:
    B_diff, W_diff = 0, 0
    for i in range(x, x + 8):
        for j in range(y, y + 8):
            if board[i][j] != B_start[i - x][j - y]:
                B_diff += 1
            if board[i][j] != W_start[i - x][j - y]:
                W_diff += 1

    return min(B_diff, W_diff)


def min_count(n, m, board) -> int:
    minimum = 50 * 50 // 2
    for i in range(n):
        for j in range(m):
            if n - i < 8 or m - j < 8:
                continue
            cur = count_recolor_point(i, j, board)
            if cur < minimum:
                minimum = cur

    return minimum


n, m = map(int, input().split())

initial_board = [list(input()) for _ in range(n)]
B_start = [[''] * 8 for _ in range(8)]
W_start = [[''] * 8 for _ in range(8)]

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            B_start[i][j] = "B"
            W_start[i][j] = 'W'
        else:
            B_start[i][j] = 'W'
            W_start[i][j] = "B"

print(min_count(n, m, initial_board))
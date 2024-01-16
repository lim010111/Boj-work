import sys
from collections import deque

input = sys.stdin.readline

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    first_man = matrix[x][y]
    matrix[x][y] = "X"

    result = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx > m - 1 or ny > n - 1:
                continue

            if first_man != matrix[nx][ny]:
                continue
            
            result += 1
            matrix[nx][ny] = "X"
            queue.append((nx, ny))

    return result ** 2


n, m = map(int, input().split())

matrix = list(list(input().rstrip()) for _ in range(m))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

w, b = 0, 0
for i in range(m):
    for j in range(n):
        if matrix[i][j] == "W":
            w += bfs(i, j)

        elif matrix[i][j] == "B":
            b += bfs(i, j)

print(w, b)
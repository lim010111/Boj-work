import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue = deque()
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if graph[k][i][j] == 1:
                    queue.append((k, i, j, 0))

    if not queue:
        return -1

    while queue:
        z, x, y, days = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx < 0 or ny < 0 or nz < 0 or nx > n - 1 or ny > m - 1 or nz > h - 1:
                continue

            if graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = 1

                queue.append((nz, nx, ny, days + 1))

        if not queue:
            for k in range(h):
                for i in range(n):
                    for j in range(m):
                        if graph[k][i][j] == 0:
                            return -1

            return days

m, n, h = map(int, input().split())

graph = [
    [list(map(int, input().split())) for _ in range(n)]
    for _ in range(h)
]


dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

print(bfs())
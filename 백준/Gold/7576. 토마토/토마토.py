import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    queue = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                queue.append((i, j, 0))
                
    if not queue:
        return -1

    while queue:
        x, y, days = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx > n - 1 or ny > m - 1:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = 1

                queue.append((nx, ny, days + 1))

        if not queue:
            for i in range(n):
                for j in range(m):
                    if graph[i][j] == 0:
                        return -1
                        
            return days
                

m, n = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs())
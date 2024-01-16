import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    queue = deque()
    queue.append((0, 0, 1, True))

    while queue:
        x, y, count, can_break = queue.popleft()

        if (x, y) == (n - 1, m - 1):
            return count

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx > n - 1 or ny > m - 1:
                continue

            if graph[nx][ny] == 0 and not visited[nx][ny][can_break]:
                visited[nx][ny][can_break] = True
                queue.append((nx, ny, count + 1, can_break))

            if graph[nx][ny] == 1 and can_break:
                queue.append((nx, ny, count + 1, False))

    return -1

n, m = map(int, input().split())

graph = []
visited = [[[False, False] for _ in range(m)] for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs())
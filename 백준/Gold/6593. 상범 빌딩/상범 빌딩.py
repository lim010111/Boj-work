from collections import deque
import sys

input = sys.stdin.readline

def bfs(z, x, y):
    queue = deque()
    queue.append((z, x, y, 0))
    graph[z][x][y] = "#"
    
    while queue:
        z, x, y, count = queue.popleft()

        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]

            if nz < 0 or nx < 0 or ny < 0 or nz > l - 1 or nx > r - 1 or ny > c - 1:
                continue

            if graph[nz][nx][ny] == "#":
                continue

            if graph[nz][nx][ny] == "E":
                return count + 1
            
            graph[nz][nx][ny] = "#"
            queue.append((nz, nx, ny, count + 1))


    return 0

while True:
    l, r, c = map(int, input().split())
    if (l, r, c) == (0, 0, 0):
        break
    
    graph = []
    for _ in range(l):
        graph.append([list(input().rstrip()) for _ in range(r)])
        input()
    
    dz = [-1, 1, 0, 0, 0, 0]
    dx = [0, 0, -1, 1, 0, 0]
    dy = [0, 0, 0, 0, 1, -1]

    for i in range(l):
        for j in range(r):
            for k in range(c):
                if graph[i][j][k] == "S":
                    result = bfs(i, j, k)

                    if not result:
                        print("Trapped!")

                    else:
                        print(f"Escaped in {result} minute(s).")
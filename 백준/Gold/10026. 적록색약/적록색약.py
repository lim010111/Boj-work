from collections import deque

def bfs(x, y, matrix, visited):
    queue = deque()
    queue.append((x, y))

    visited[x][y] = True
    target_color = matrix[x][y]
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx > n - 1 or ny > n - 1:
                continue

            if visited[nx][ny]:
                continue

            if matrix[nx][ny] != target_color:
                continue

            visited[nx][ny] = True
            queue.append((nx, ny))

    return 1

            

n = int(input())
paint = [list(input()) for _ in range(n)]
paint_visited = [[False for _ in range(n)] for _ in range(n)]

paint_blinded = [elem[:] for elem in paint]
for i in range(n):
    for j in range(n):
        if paint_blinded[i][j] == "R":
            paint_blinded[i][j] = "G"
paint_blinded_visited = [[False for _ in range(n)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0
for i in range(n):
    for j in range(n):
        if not paint_visited[i][j]:
            result += bfs(i, j, paint, paint_visited)

result_blinded = 0
for i in range(n):
    for j in range(n):
        if not paint_blinded_visited[i][j]:
            result_blinded += bfs(i, j, paint_blinded, paint_blinded_visited)

print(result, result_blinded)
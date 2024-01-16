from collections import deque
import sys

input = sys.stdin.readline


def bfs():
    queue = deque()

    for i in range(r):
        for j in range(c):
            if matrix[i][j] == "J":
                queue.append((i, j, 0))

    for i in range(r):
        for j in range(c):
            if matrix[i][j] == "F":
                queue.append((i, j, 0))

    while queue:
        x, y, cnt = queue.popleft()
        if matrix[x][y] == "J":
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or ny < 0 or nx > r - 1 or ny > c - 1:
                    return cnt + 1
    
                if matrix[nx][ny] != ".":
                    continue
    
                matrix[nx][ny] = "J"
                queue.append((nx, ny, cnt + 1))

    
        else:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
            
                if nx < 0 or ny < 0 or nx > r - 1 or ny > c - 1:
                    continue
                if matrix[nx][ny] == "F" or matrix[nx][ny] == "#":
                    continue

                matrix[nx][ny] = "F"
                queue.append((nx, ny, 0))
        matrix[x][y] = "#"
    return "IMPOSSIBLE"


r, c = map(int, input().split())

matrix = [list(input().rstrip()) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs())
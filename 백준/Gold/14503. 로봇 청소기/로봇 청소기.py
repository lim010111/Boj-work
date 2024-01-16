import sys
from collections import deque
input = sys.stdin.readline

def around(x, y, d):
    for _ in range(4):
        if graph[x + dx[d - 1]][y + dy[d - 1]] != 0:
            d -= 1
            if d < 0:
                d = 3
        else:
            return "spin", d - 1

    if graph[x - dx[d]][y - dy[d]] != 1:
        return "back", d

    return "end", 0

def dfs(x, y, d):
    queue = deque()
    queue.append((x, y, d))
    cleaned = 1
    graph[x][y] = "c"

    while queue:
        x, y, d = queue.popleft()

        result, d = around(x, y, d)
        if result == "end":
            return cleaned

        elif result == "spin":
            if d < 0:
                d += 4
            graph[x + dx[d]][y + dy[d]] = "c"
            cleaned += 1
            queue.append((x + dx[d], y + dy[d], d))

        else:
            queue.append((x - dx[d], y - dy[d], d))
            
    return cleaned

        
        
        

n, m = map(int, input().split())
r, c, d = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

# indexing for variation d
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

print(dfs(r, c, d))
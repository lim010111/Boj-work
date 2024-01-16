import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.readline


def around(x, y):
    count = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if graph[nx][ny] == 0:
            count += 1

    return count


def dfs(x, y):
    if graph[x][y] != 0 and not visited[x][y]:
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)

        return True

    return False


r, c = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]
graph_arounded = [[0 for _ in range(c)] for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

year = 0
while True:
    result = 0

    visited = [[False for _ in range(c)] for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if dfs(i, j):
                result += 1

    if result > 1:
        print(year)
        break

    for i in range(r):
        for j in range(c):
            if graph[i][j] != 0:
                graph_arounded[i][j] = around(i, j)

    for i in range(r):
        for j in range(c):
            graph[i][j] -= graph_arounded[i][j]
            if graph[i][j] < 0:
                graph[i][j] = 0

    if graph == [[0 for _ in range(c)] for _ in range(r)]:
        print(0)
        break
        
    year += 1
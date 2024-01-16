import sys
from collections import deque

input = sys.stdin.readline

def dfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[0] = True

    while queue:
        x, y = queue.popleft()

        if (x, y) == (spots[-1][0], spots[-1][1]):
            return "happy"

        for i in range(n + 2):
            if abs(x - spots[i][0]) + abs(y - spots[i][1]) > 1000 or visited[i]:
                continue
            
            visited[i] = True
            queue.append(spots[i])
    return "sad"

for _ in range(int(input())):
    n = int(input())
    spots = [tuple(map(int, input().split())) for _ in range(n + 2)]
    visited = [False] * (n + 2)

    x0, y0 = spots[0]
    print(dfs(x0, y0))
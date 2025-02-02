from collections import deque
from sys import stdin

input = stdin.readline

def findParentNode(neighbors):
    queue = deque([1])
    visited[1] = True

    result = [0] * (n + 1)

    while queue:
        x = queue.popleft()

        for elem in neighbors[x]:
            if not visited[elem]:
                result[elem] = x
                visited[elem] = True
                queue.append(elem)

    return result[2:]


n = int(input())

neighbors = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(1, n):
    a, b = map(int, input().split())

    neighbors[a].append(b)
    neighbors[b].append(a)

print("\n".join(map(str, findParentNode(neighbors))))
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(start: int, acc: int):

    visited[start] = True

    global farthest_node, max_distance
    if acc > max_distance:
        max_distance = acc
        farthest_node = start

    for node, weight in tree[start]:
        if not visited[node]:
            dfs(node, acc + weight)


v = int(input())

tree = [[] for _ in range(v + 1)]
for _ in range(v):
    line = list(map(int, input().split()))
    node, info = line[0], line[1:-1]

    for i in range(0, len(info), 2):
        neighbor, weight = info[i : i + 2]

        tree[node].append((neighbor, weight))

visited = [False for _ in range(v + 1)]

# 가장 거리가 먼 노드 찾기
farthest_node = 0
max_distance = 0
dfs(1, 0)
visited = [False for _ in range(v + 1)]

# 가장 먼 거리인, 트리의 지름 찾기
max_distance = 0
dfs(farthest_node, 0)

print(max_distance)
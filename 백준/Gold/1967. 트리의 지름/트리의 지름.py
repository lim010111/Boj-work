import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node, acc):
    visited[node] = True
    global farthest_node, max_distance
    if acc > max_distance:
        max_distance = acc
        farthest_node = node
    for nxt, w in nodes[node]:
        if not visited[nxt]:
            dfs(nxt, acc + w)

n = int(input())
nodes = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    nodes[u].append((v, w))
    nodes[v].append((u, w))

visited = [False] * (n + 1)
max_distance = 0
farthest_node = 0
dfs(1, 0)

visited = [False] * (n + 1)
max_distance = 0
dfs(farthest_node, 0)

print(max_distance)

# DFS와 BFS
# https://www.acmicpc.net/problem/1260


class Find:
    def __init__(self, n, m, v, neighbors):
        self.neighbors = neighbors
        self.visited = [False] * (n + 1)
        self.dfs_log = []
        self.bfs_log = []

    def dfs(self, start):
        # print(start)
        self.visited[start] = True
        self.dfs_log.append(start)

        for neighbor in neighbors[start]:
            if not self.visited[neighbor]:
                self.dfs(neighbor)  # 왜 함수도 self로 호출해야 하는 걸까?

        return

    def bfs(self, start):
        from collections import deque

        queue = deque([start])
        self.visited[start] = True
        self.bfs_log.append(start)
        # print(self.visited)

        while queue:
            s = queue.popleft()

            # print(self.visited)
            for neighbor in self.neighbors[s]:
                if not self.visited[neighbor]:
                    queue.append(neighbor)
                    self.visited[neighbor] = True
                    self.bfs_log.append(neighbor)

        return


if __name__ == "__main__":
    n, m, v = map(int, input().split())

    neighbors = [[] for _ in range(n + 1)]
    for _ in range(m):
        # print("입력")
        a, b = map(int, input().split())
        neighbors[a].append(b)
        neighbors[b].append(a)
    neighbors = [sorted(elem) for elem in neighbors]

    # print(neighbors)

    dfs_find = Find(n, m, v, neighbors)
    bfs_find = Find(n, m, v, neighbors)
    dfs_find.dfs(v)
    bfs_find.bfs(v)
    print(*dfs_find.dfs_log)
    print(*bfs_find.bfs_log)
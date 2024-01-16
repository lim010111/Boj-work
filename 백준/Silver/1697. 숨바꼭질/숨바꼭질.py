from collections import deque

def bfs(start):
    queue = deque([(start, 0)])
    visited[start] = True

    while queue:
        v, c = queue.popleft()
        nv = 0

        for i in range(3):
            if i == 0:
                nv = v + 1
            if i == 1:
                nv = v - 1
            if i == 2:
                nv = v * 2

            if nv > k + 1 or nv < 0:
                continue
            
            if visited[nv]:
                continue
            
            if nv == k:
                return c + 1
                
            visited[nv] = True
            queue.append((nv, c + 1))

n, k = map(int, input().split())

if k > n:
    visited = [False for _ in range(k + 2)]
    print(bfs(n))
else:
    print(n - k)
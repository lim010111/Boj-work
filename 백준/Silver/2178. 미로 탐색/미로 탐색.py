from collections import deque

def bfs(n, m):
    matrix = [list(map(int, list(input()))) for _ in range(n)]
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    start = None
    for r in range(n):
        for c in range(m):
            if matrix[r][c] == 1:
                start = (r, c)
                break
        if start is not None:
            break
    
    
    queue: deque[tuple] = deque([start])

    while queue:
        r, c = queue.popleft()

        for move in moves:
            nr = r + move[0]
            nc = c + move[1]

            if nr < 0 or nc < 0 or nr >= n or nc >= m:
                continue

            if matrix[nr][nc] != 1:
                continue

            matrix[nr][nc] += matrix[r][c]
            if (nr, nc) == (n - 1, m - 1):
                return matrix[nr][nc]
            
            queue.append((nr, nc))


if __name__ == "__main__":
    n, m = map(int, input().split())

    print(bfs(n, m))
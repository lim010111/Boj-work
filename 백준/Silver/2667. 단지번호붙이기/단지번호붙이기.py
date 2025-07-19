from collections import deque

def bfs(r, c) -> int:
    queue = deque([(r, c)])
    matrix[r][c] = 0
    count = 1

    while queue:
        r, c = queue.popleft()

        for movement in movements:
            nr = r + movement[0]
            nc = c + movement[1]

            if nr < 0 or nr >= n or nc < 0 or nc >= n:
                continue

            if matrix[nr][nc] == 0:
                continue
            
            matrix[nr][nc] = 0
            count += 1
            queue.append((nr, nc))

    return count

if __name__ == "__main__":
    n = int(input())
    matrix = [list(map(int, list(input()))) for _ in range(n)]
    movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    result = []

    for r in range(n):
        for c in range(n):
            if matrix[r][c] == 1:
                result.append(bfs(r, c))

    result.sort()
    print(len(result))
    print(*result, sep="\n")
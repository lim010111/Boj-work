from collections import deque
import sys

input = sys.stdin.readline

def shortest_path():
    movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[[False, False] for _ in range(columns)] for _ in range(rows)]

    queue = deque()
    queue.append((0, 0, 1, True))
    visited[0][0][0] = True

    while queue:
        # print()
        # [print(''.join(elem)) for elem in matrix]
        r, c, move, breakable = queue.popleft()

        if (r, c) == (rows - 1, columns - 1):
            return move

        for x, y in movements:
            nr = r + x
            nc = c + y

            if nr < 0 or nc < 0 or nr >= rows or nc >= columns:
                continue

            if not breakable:
                if not visited[nr][nc][1] and matrix[nr][nc] == '0':
                    visited[nr][nc][1] = True
                    queue.append((nr, nc, move + 1, False))

            else:
                if not visited[nr][nc][0]:
                    if matrix[nr][nc] == '1':
                        visited[nr][nc][1] = True
                        queue.append((nr, nc, move + 1, False))
        
                    else:
                        visited[nr][nc][0] = True
                        queue.append((nr, nc, move + 1, True))
    return -1


if __name__ == "__main__":
    rows, columns = map(int, input().split())
    matrix = [list(input().rstrip()) for _ in range(rows)]
    print(shortest_path())
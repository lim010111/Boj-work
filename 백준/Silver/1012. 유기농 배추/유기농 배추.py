from collections import deque
def bfs(start_r, start_c) -> None:
    movements = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상, 하, 좌, 우

    queue = deque([(start_r, start_c)])
    matrix[start_r][start_c] = 0

    while queue:
        r, c = queue.popleft()

        for movement in movements:
            nxt_r = r + movement[0]
            nxt_c = c + movement[1]
            
            if nxt_r < 0 or nxt_c < 0 or nxt_r >= rows or nxt_c >= cols:
                continue

            if matrix[nxt_r][nxt_c] == 0:
                continue

            matrix[nxt_r][nxt_c] = 0
            queue.append((nxt_r, nxt_c))

if __name__ == "__main__":
    for _ in range(int(input())):
        cols, rows, points = map(int, input().split())
        matrix = [[0 for _ in range(cols)] for _ in range(rows)]

        for _ in range(points):
            col, row = map(int, input().split())
            matrix[row][col] = 1

        count = 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 1:
                    bfs(r, c)
                    count += 1

        print(count)
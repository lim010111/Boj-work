from collections import deque

def min_days(rows, cols, storage):
    # 익은 토마토 position 구한 후 대기열에 넣기
    queue = deque([])
    
    for r in range(rows):
        for c in range(cols):
            if storage[r][c] == 1:
                queue.append((r, c, 0))
    # 대기열에 있는 토마토들 순회하며 bfs
    
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    last_day = 0
    while queue:
        r, c, day = queue.popleft()
        if day > last_day:
            last_day = day
        
        for x, y in moves:
            nr = r + x
            nc = c + y

            if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                continue

            if storage[nr][nc] == 0:
                storage[nr][nc] = 1
                queue.append((nr, nc, day + 1))
        
    # 탐색이 모두 끝나면 다 익음. return
    for r in range(rows):
        for c in range(cols):
            if storage[r][c] == 0:
                return -1
    return last_day
    
if __name__ == "__main__":
    cols, rows = map(int, input().split()) # 열, 행
    storage = [list(map(int, input().split())) for _ in range(rows)]
    print(min_days(rows, cols, storage))
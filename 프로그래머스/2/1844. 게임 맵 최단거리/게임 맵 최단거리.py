from collections import deque

def solution(maps):
    rows, cols = (len(maps), len(maps[0]))
    moves = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    queue = deque([(0, 0)])
    maps[0][0] = 1

    while queue:
        r, c = queue.popleft()
        if (r, c) == (rows - 1, cols - 1):
            return maps[r][c]
        for move in moves:
            next_r = r + move[0]
            next_c = c + move[1]

            if next_r < 0 or next_r >= rows or next_c < 0 or next_c >= cols:
                continue
        
            if maps[next_r][next_c] != 1:
                continue

            maps[next_r][next_c] = maps[r][c] + 1
            queue.append((next_r, next_c))
    
    return -1
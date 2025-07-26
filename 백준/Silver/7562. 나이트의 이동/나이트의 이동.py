from collections import deque

def bfs(l, start_pos, target_pos):

    if start_pos == target_pos:
        return 0
    
    chessboard = [[0 for _ in range(l)] for _ in range(l)]
    moves = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
    queue = deque([tuple(start_pos)])

    while queue:
        r, c = queue.popleft()

        for x, y in moves:
            nr = r + x
            nc = c + y

            if nr < 0 or nc < 0 or nr >= l or nc >= l:
                continue

            if chessboard[nr][nc] != 0:
                continue
            
            if (nr, nc) == target_pos:
                return chessboard[r][c] + 1
            
            chessboard[nr][nc] += chessboard[r][c] + 1
            queue.append((nr, nc))
    


if __name__ == "__main__":
    for _ in range(int(input())):
        l = int(input())
        pos = tuple(map(int, input().split()))
        target_pos = tuple(map(int, input().split()))

        min_move = bfs(l, pos, target_pos)
        print(min_move)
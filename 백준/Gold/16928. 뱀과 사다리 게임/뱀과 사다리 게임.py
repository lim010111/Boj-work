from collections import deque
from sys import stdin

input = stdin.readline

def solution():
    queue = deque([(1, 0)])


    moves = [1, 2, 3, 4, 5, 6]
    while queue:
        pos, count = queue.popleft()

        for move in moves:
            nxt_pos = pos + move

            if nxt_pos in ladder_info:
                nxt_pos = ladder_info[nxt_pos]

            elif nxt_pos in snake_info:
                nxt_pos = snake_info[nxt_pos]

            if game_map[nxt_pos]:
                continue

            if nxt_pos == 100:
                return count + 1

            game_map[nxt_pos] = True
            queue.append((nxt_pos, count + 1))

if __name__ == "__main__":
    game_map = {i:False for i in range(1, 100 + 1)}

    ladder_info = {}
    snake_info = {}
    n, m = map(int, input().split())

    for _ in range(n):
        start, end = map(int, input().split())
        ladder_info[start] = end

    for _ in range(m):
        start, end = map(int, input().split())
        snake_info[start] = end

    print(solution())
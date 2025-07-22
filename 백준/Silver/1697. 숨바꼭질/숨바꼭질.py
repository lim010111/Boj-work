# https://www.acmicpc.net/problem/1697
# 숨바꼭질

from collections import deque

def find(pos, target):

    if pos == target:
        return 0

    if target < pos:
        return pos - target

    moves =  [-1, 1, 2]
    visited = [False] * (2 * target + 1) if target <= 50000 else [False] * 100001

    queue = deque([(pos, 0)])
    visited[pos] = True

    while queue:
        # print(queue)
        p, t = queue.popleft()

        for i in range(3):
            if i == 2:
                nxt_p = p * 2
            else:
                nxt_p = p + moves[i]

            if nxt_p < 0 or nxt_p > 2 * target or nxt_p > 100000:
                continue

            if visited[nxt_p]:
                continue
            
            if nxt_p == target:
                return t + 1

            visited[nxt_p] = True
            queue.append((nxt_p, t + 1))


if __name__ == "__main__":
    pos, target = map(int, input().split())

    result = find(pos, target)
    print(result)
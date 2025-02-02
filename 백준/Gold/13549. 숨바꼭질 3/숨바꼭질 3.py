from collections import deque


def hide_and_seek_3(n: int, k: int) -> int:

    if n > k:
        return n - k

    queue = deque([(n, 0)])
    visited = {n}

    while queue:
        x, t = queue.popleft()

        if x == k:
            return t

        for i in range(3):

            if i == 0:
                nx = x * movement[i]
                nt = t

            else:
                nx = x + movement[i]
                nt = t + 1

            if nx > k + 1 or nx < 0:
                continue

            if nx in visited:
                continue

            visited.add(nx)
            queue.append((nx, nt))

    return 0


n, k = map(int, input().split())
movement = [2, -1, 1]

print(hide_and_seek_3(n, k))
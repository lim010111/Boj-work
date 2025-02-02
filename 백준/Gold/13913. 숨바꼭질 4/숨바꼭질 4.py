from collections import deque


def hide_and_seek_4(n, k):

    if n > k:
        return n - k, list(range(n, k - 1, -1))

    
    queue = deque([(n, 0, [n])])

    while queue:
        x, t, trace = queue.popleft()

        if x == k:
            return t, trace

        for i in range(3):
            if i == 2:
                nx = x * movement[i]

            else:
                nx = x + movement[i]

            if nx in visited:
                continue

            if nx > k + 1 or nx < 0:
                continue

            nt = t + 1
            n_trace = trace[:]
            n_trace.append(nx)

            visited.add(nx)
            queue.append((nx, nt, n_trace))

    return 0, [0]


n, k = map(int, input().split())
movement = [-1, 1, 2]
visited = {n}

result = hide_and_seek_4(n, k)

print(result[0], " ".join(map(str, result[1])), sep="\n")
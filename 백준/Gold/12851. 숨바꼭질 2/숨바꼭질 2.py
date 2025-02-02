from collections import deque


def hide_and_seek2(n, k, visited_set):

    if n == k:
        return 0, 1

    if n > k:
        if n == 2 and k == 1:
            return 1, 2
        return n - k, 1

    queue = deque([(n, 0)])
    course_count = 0
    min_time = 0
    temp_time = 0
    dp_set = set()

    while queue:
        position, time = queue.popleft()

        if time > temp_time:
            visited_set |= dp_set
            dp_set = set()
            temp_time = time

        if position == k:
            if course_count != 0 and time > min_time:
                break

            course_count += 1
            min_time = time

        for i, movement in enumerate(movements):
            next_position = position * movement if i == 2 else position + movement

            if next_position in visited_set:
                continue

            if next_position > k + 1:
                continue

            if next_position < 0:
                continue

            dp_set.add(next_position)
            queue.append((next_position, time + 1))

    return min_time, course_count


n, k = map(int, input().split())

movements = [-1, 1, 2]
visited_set = {n}

results = list(hide_and_seek2(n, k, visited_set))

print(results[0], results[1], sep="\n")
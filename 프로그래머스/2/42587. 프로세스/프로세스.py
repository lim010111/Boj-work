from collections import deque

def solution(priorities, location):
    count = 0
    priorities_queue = deque(priorities)
    location_queue = deque(range(len(priorities)))

    while priorities_queue:
        cur_priority = priorities_queue.popleft()
        cur_location = location_queue.popleft()

        if priorities_queue and cur_priority < max(priorities_queue):
            priorities_queue.append(cur_priority)
            location_queue.append(cur_location)
            continue

        count += 1
        if location == cur_location:
            return count
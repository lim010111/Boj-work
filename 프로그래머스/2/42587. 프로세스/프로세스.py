from collections import deque

def solution(priorities, location):
    count = 0
    queue = deque(enumerate(priorities))

    while queue:
        initial_location, priority = queue.popleft()

        if queue and priority < max(queue, key=lambda x: x[1])[1]: # empty queue 예외처리
            queue.append((initial_location, priority))
            continue

        count += 1
        
        if location == initial_location:
            return count
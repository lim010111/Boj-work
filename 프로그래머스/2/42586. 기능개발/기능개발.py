from collections import deque
import math

def solution(progresses, speeds):
    answer = []

    n = len(progresses)
    remain_times = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(n)]
    
    cur_remain_time = remain_times[0]
    queue = deque(remain_times[1:])
    streak = 1
    while queue:
        remain_time = queue.popleft()

        if cur_remain_time >= remain_time:
            streak += 1

        else:
            cur_remain_time = remain_time
            answer.append(streak)
            streak = 1

    answer.append(streak)

    return answer
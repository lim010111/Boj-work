from typing import List
from collections import deque

def solution(progresses: List[int], speeds: List[int]) -> List[int]:

    progresses = deque(progresses)
    speeds = deque(speeds)

    result = []
    release = 0

    while progresses:
        while progresses and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            release += 1
        
        if release != 0: 
            result.append(release)
            release = 0

        for i in range(len(progresses)):
            progresses[i] += speeds[i]

    return result
from collections import deque
from typing import List


def solution(arr: List) -> List:

    arr = deque(arr)
    result = [arr.popleft()]

    while arr:
        selected = arr.popleft()
        if selected != result[-1]:
            result.append(selected)

    return result
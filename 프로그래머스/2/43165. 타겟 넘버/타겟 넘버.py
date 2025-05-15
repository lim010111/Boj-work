from typing import List
from collections import deque


def solution(numbers: List[int], target: int) -> int:
    answer = 0

    def find(index, s):
        nonlocal answer
        if index == len(numbers):
            if s == target:
                answer += 1
            return

        find(index + 1, s + numbers[index])
        find(index + 1, s - numbers[index])

    find(0, 0)

    return answer
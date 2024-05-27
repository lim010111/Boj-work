from typing import List


def solution(nums: List) -> int:
    kinds = set()

    for num in nums:
        kinds.add(num)

    return min(len(kinds), len(nums) // 2)

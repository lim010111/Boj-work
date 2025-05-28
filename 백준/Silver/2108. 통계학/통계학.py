from sys import stdin
from collections import defaultdict
from typing import List

input = stdin.readline


def solution(n: int, nums: List[int]) -> None:
    # 산술평균
    average = sum(nums) / n

    # 중앙값
    mid_num = sorted(nums)[int(n/2)]

    # 최빈값
    counter_nums = defaultdict(int)
    for num in nums:
        counter_nums[num] += 1
        
    max_count = max(counter_nums.values())

    nums_max_counts = []
    for key, value in counter_nums.items():
        if value == max_count:
            nums_max_counts.append(key)

    if len(nums_max_counts) > 1:
        mode = sorted(nums_max_counts)[1]
    else:
        mode = nums_max_counts[0]
    
    # 범위
    range_nums = max(nums) - min(nums)

    print(round(average), mid_num, mode, range_nums, sep="\n")


n = int(input())
nums = [int(input()) for _ in range(n)]

solution(n, nums)
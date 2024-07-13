from typing import List

def choosingNumber(n: int, k: int, nums: List) -> int:
    nums.sort(reverse = True)
    return sum(nums[:k]) - sum(range(1, k))

n, k = map(int, input().split())
nums = list(map(int, input().split()))

print(choosingNumber(n, k, nums))
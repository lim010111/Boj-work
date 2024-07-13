from sys import stdin
from typing import List

input = stdin.readline

def minCost(n: int, prices: List) -> int:
    
    if len(prices) > 2:
        return sum(prices) - sum(prices[2::3])
    else:
        return sum(prices)

n = int(input())

prices = sorted([int(input()) for _ in range(n)], reverse = True)


print(minCost(n, prices))
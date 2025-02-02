from typing import List


def rgb_distance(n: int, rgb_cost: List[List[int]]) -> int:
    for i in range(1, n):
        rgb_cost[i][0] += min(rgb_cost[i - 1][1], rgb_cost[i - 1][2])
        rgb_cost[i][1] += min(rgb_cost[i - 1][0], rgb_cost[i - 1][2])
        rgb_cost[i][2] += min(rgb_cost[i - 1][0], rgb_cost[i - 1][1])

    return min(rgb_cost[-1])


n = int(input())
rgb_cost = [list(map(int, input().split())) for _ in range(n)]

print(rgb_distance(n, rgb_cost))
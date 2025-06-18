import sys
from typing import List

input = sys.stdin.readline


def max_cost(n: int, costs: List[int]):
    dp_costs = [cost[:] for cost in costs]

    for i in range(1, n):
        for j in range(len(dp_costs[i])):
            if j == 0:
                dp_costs[i][j] += dp_costs[i-1][j]
                continue

            if j == len(dp_costs[i]) - 1:
                dp_costs[i][j] += dp_costs[i-1][-1]
                continue

            dp_costs[i][j] += max(dp_costs[i-1][j-1], dp_costs[i-1][j])

    return max(dp_costs[-1])

                
if __name__ == "__main__":
    n = int(input())
    costs = [list(map(int, input().split())) for _ in range(n)]
    answer = max_cost(n, costs)
    print(answer)
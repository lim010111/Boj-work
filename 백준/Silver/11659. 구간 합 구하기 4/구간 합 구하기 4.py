import sys

input = sys.stdin.readline

class Solution():
    def __init__(self, n, nums):
        self.cumulative_sum = [0] * (n + 1)
        for i in range(n):
            self.cumulative_sum[i + 1] += self.cumulative_sum[i] + nums[i]

    def answer(self, i, j):
        return self.cumulative_sum[j] - self.cumulative_sum[i-1]

if __name__ == "__main__":
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    solution = Solution(n, nums)
    for _ in range(m):
        i, j = map(int, input().split())
        print(solution.answer(i, j))
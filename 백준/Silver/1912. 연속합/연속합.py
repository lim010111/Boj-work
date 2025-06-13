from typing import List

class Solution():
    def __init__(self, n: int, nums: List[int]):
        self.n = n
        self.seq = nums
        self.max_seq_sums = [0] * n
        self.max_seq_sums[0] = nums[0]

    def answer(self):
        for i in range(n - 1):
            self.max_seq_sums[i + 1] = max(self.max_seq_sums[i] + self.seq[i + 1], self.seq[i + 1])

        return max(self.max_seq_sums)
            

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    solution = Solution(n, nums)
    print(solution.answer())
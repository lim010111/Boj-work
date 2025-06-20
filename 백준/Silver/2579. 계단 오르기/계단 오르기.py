from typing import List
import sys

input = sys.stdin.readline


def max_score(n: int, scores: List[int]) -> int:
    if n == 1:
        return scores[0]
    dp = [0] * n
    dp[0] = scores[0]
    dp[1] = scores[0] + scores[1]
    
    for i in range(2, n):
        dp[i] = max(dp[i - 2] + scores[i], dp[i - 3] + scores[i - 1] + scores[i])

    return dp[-1]
        

if __name__ == "__main__":
    n = int(input())
    scores = [int(input()) for _ in range(n)]
    answer = max_score(n, scores)
    print(answer)
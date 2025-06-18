import sys
from typing import List

input = sys.stdin.readline


def rgb_distance(n: int, matrix: List[int]) -> int:
    for i in range(1, n):
        for j in range(3):
            matrix[i][j] += min(matrix[i-1][:j] + matrix[i-1][j+1:])


    distance = min(matrix[-1])

    return distance

if __name__ == "__main__":
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    distance = rgb_distance(n, matrix)
    print(distance)
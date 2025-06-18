import sys
from typing import List

input = sys.stdin.readline


def rgb_distance(n: int, matrix: List[int]) -> int:
    for i in range(1, n):
        matrix[i][0] = matrix[i][0] + min(matrix[i-1][1], matrix[i-1][2])
        matrix[i][1] = matrix[i][1] + min(matrix[i-1][0], matrix[i-1][2])
        matrix[i][2] = matrix[i][2] + min(matrix[i-1][0], matrix[i-1][1])


    distance = min(matrix[-1])

    return distance

if __name__ == "__main__":
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    distance = rgb_distance(n, matrix)
    print(distance)
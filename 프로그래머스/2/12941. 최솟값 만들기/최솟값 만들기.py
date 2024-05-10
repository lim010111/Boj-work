from typing import List

def solution(A: List[int], B: List[int]) -> int:
    length = len(A)
    result = 0

    A.sort()
    B.sort(reverse=True)

    for i in range(length):
        result += A[i] * B[i]

    return result
import sys

input = sys.stdin.readline


def solution(n: int):
    if n == 1:
        return 1
    if n == 2:
        return 2

    s2, s1 = 2, 1
    for i in range(n-2):
        s2, s1 = (s2+s1) % 15746, s2


    return s2

if __name__ == "__main__":
    n = int(input())
    print(solution(n))
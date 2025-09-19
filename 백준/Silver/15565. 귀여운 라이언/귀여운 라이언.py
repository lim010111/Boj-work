from sys import stdin

input = stdin.readline


def solution():
    indices_lion = [i for i in range(N) if dolls[i] == "1"]

    if K > len(indices_lion):
        return -1

    min_size = float("inf")
    for i in range(len(indices_lion) - K + 1):
        cur_size = indices_lion[i + K - 1] - indices_lion[i] + 1
        min_size = min(cur_size, min_size)

    return min_size


if __name__ == "__main__":
    N, K = map(int, input().split())
    dolls = input().split()

    answer = solution()
    print(answer)
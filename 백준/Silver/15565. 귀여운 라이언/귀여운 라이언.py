from sys import stdin

input = stdin.readline


def solution():
    indices_lion, lions = [], 0
    for idx, doll in enumerate(dolls):
        if doll == "1":
            indices_lion.append(idx)
            lions += 1

    if K > lions:
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
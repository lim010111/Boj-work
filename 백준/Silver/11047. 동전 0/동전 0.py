import sys

input = sys.stdin.readline


def solve():
    current_cost = K

    i = N - 1
    counts = 0
    while current_cost != 0:
        if current_cost < kinds[i]:
            i -= 1
            continue

        counts += current_cost // kinds[i]
        current_cost = current_cost % kinds[i]

    return counts


if __name__ == "__main__":
    N, K = map(int, input().split())
    kinds = [int(input()) for _ in range(N)]
    answer = solve()
    print(answer)
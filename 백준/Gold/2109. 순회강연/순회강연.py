from sys import stdin

input = stdin.readline


def max_earnings(n, works):
    earnings = 0

    scheduled = [False] * (max_deadline + 1)
    sorted_works = sorted(works, reverse=True)

    for pay, deadline in sorted_works:
        for i in range(deadline, 0, -1):
            if not scheduled[i]:
                scheduled[i] = True
                earnings += pay
                break

    return earnings


if __name__ == "__main__":
    n = int(input())

    max_deadline = 0
    works = []
    for _ in range(n):
        pay, deadline = map(int, input().split())
        works.append((pay, deadline))

        if deadline > max_deadline:
            max_deadline = deadline

    print(max_earnings(n, works))
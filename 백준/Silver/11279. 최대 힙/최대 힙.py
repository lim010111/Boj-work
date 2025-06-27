import sys
import heapq


def solve():
    li = []
    heapq.heapify(li)
    for _ in range(int(input())):
        cal = int(sys.stdin.readline())

        if cal == 0:
            if li:
                print(-heapq.heappop(li))
            else:
                print(0)
        else:
            heapq.heappush(li, -cal)


if __name__ == "__main__":
    solve()
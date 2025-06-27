import sys
import heapq


input = sys.stdin.readline


def solve():
    li = []
    heapq.heapify(li)

    for _ in range(int(input())):
        cal = int(input())
        if cal == 0:
            if not li:
                sys.stdout.write("0\n")
            else:
                popped = heapq.heappop(li)[1]
                sys.stdout.write(str(popped) + "\n")

        else:
            heapq.heappush(li, (abs(cal), cal))


if __name__ == "__main__":
    solve()
import sys
import heapq

input = sys.stdin.readline


def solve():
    results = []
    m = int(input())
    lines = m // 10 + 1 if m % 10 != 0 else m // 10
    max_heap, min_heap = [], []
    heapq.heapify(max_heap)
    heapq.heapify(min_heap)
    for line in range(lines):
        for i, num in enumerate(map(int, input().split())):
            if len(max_heap) == len(min_heap):
                heapq.heappush(max_heap, -num)
            else:
                heapq.heappush(min_heap, num)

            if min_heap and -max_heap[0] > min_heap[0]:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
                heapq.heappush(max_heap, -heapq.heappop(min_heap))

            if i % 2 == 0:
                results.append(-max_heap[0])

    print(m // 2 + 1)
    for i, mid in enumerate(results):
        if i != 0 and i % 10 == 0:
            print()
        print(mid, end=" ")
    print()


if __name__ == "__main__":
    test_case = int(input())
    for _ in range(test_case):
        solve()

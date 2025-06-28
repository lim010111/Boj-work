import sys
import heapq

input = sys.stdin.readline

def solve():
    n = int(input())
    
    top_n = list(map(int, input().split()))
    heapq.heapify(top_n)
    for _ in range(n - 1):
        for num in map(int, input().split()):
            if num > top_n[0]:
                heapq.heapreplace(top_n, num)

    return top_n[0]

if __name__ == "__main__":
    ans = solve()
    print(ans)
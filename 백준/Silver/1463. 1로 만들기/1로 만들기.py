from collections import deque

def solve(n):
    queue = deque([(n, 0)])

    while queue:
        cur, count = queue.popleft()
        if cur == 1:
            return count

        if cur % 3 == 0:
            queue.append((cur // 3, count + 1))

        if cur % 2 == 0:
            queue.append((cur // 2, count + 1))

        queue.append((cur - 1, count + 1))
        
    


if __name__ == "__main__":
    n = int(input())
    answer = solve(n)
    print(answer)
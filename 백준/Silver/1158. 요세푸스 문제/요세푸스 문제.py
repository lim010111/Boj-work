from collections import deque

def solution(n, k) -> str:
    result_seq = []
    queue = deque(range(1, n + 1))

    while queue:
        for i in range(k - 1):
            queue.append(queue.popleft())
        result_seq.append(queue.popleft())

    print(f"<{', '.join(map(str, result_seq))}>")
    

if __name__ == "__main__":
    n, k = map(int, input().split())
    solution(n, k)
def solution(seq):
    if len(seq) == m:
        print(*seq)
        return

    for num in range(1, n + 1):
        seq.append(num)
        solution(seq)
        seq.pop()

if __name__ == "__main__":
    n, m = map(int, input().split())
    solution([])
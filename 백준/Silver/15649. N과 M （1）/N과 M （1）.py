def solution(n, m, seq):
    if len(seq) == m:
        seqs.append(seq[:])
        return

    for i in range(1, n + 1):
        if i not in set(seq):
            seq.append(i)
            solution(n, m, seq)
            seq.pop()
    

if __name__ == "__main__":
    n, m = map(int, input().split())
    seqs = []
    solution(n, m, [])
    [print(*seq) for seq in seqs]
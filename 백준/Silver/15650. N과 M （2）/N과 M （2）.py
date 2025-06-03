def solution(n, m, seq):
    if len(seq) == m:
        seqs.add(tuple(sorted(seq)))
        return

    for num in range(1, n + 1):
        if num not in set(seq):
            seq.append(num)
            solution(n, m, seq)
            seq.pop()
            

if __name__ == "__main__":
    n, m = map(int, input().split())

    seqs = set()
    solution(n, m, [])
    [print(*seq) for seq in sorted(seqs)]
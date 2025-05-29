from sys import stdin
from typing import List
from collections import defaultdict

input = stdin.readline


def solution(n: int, m: int) -> List[str]:

    word_count = defaultdict(int)
    
    for _ in range(n):
        word = input().rstrip()
        if len(word) < m:
            continue
        word_count[word] += 1

    return sorted(word_count, key=lambda w: (-word_count[w], -len(w), w))

        

n, m = map(int, input().split())

print(*solution(n, m), sep="\n")
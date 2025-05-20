from sys import stdin
input = stdin.readline


n = int(input())
words = sorted(set(input().rstrip() for _ in range(n)), key=lambda word: (len(word), word))
print(*words, sep="\n")
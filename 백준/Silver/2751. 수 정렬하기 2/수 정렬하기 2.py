from sys import stdin
input = stdin.readline

n = int(input())
answer = sorted([int(input()) for _ in range(n)])
print(*answer, sep="\n")
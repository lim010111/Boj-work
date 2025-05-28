from sys import stdin
from collections import defaultdict

input = stdin.readline


is_dancing = defaultdict(bool)
is_dancing["ChongChong"] = True

n = int(input())
for _ in range(n):
    a, b = input().split()

    if is_dancing[a] or is_dancing[b]:
        is_dancing[a] = True
        is_dancing[b] = True

count = 0
for name in is_dancing:
    if is_dancing[name]:
        count += 1

print(count)
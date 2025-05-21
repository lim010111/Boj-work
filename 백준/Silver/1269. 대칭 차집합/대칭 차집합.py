from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
a = set(input().split())
b = set(input().split())

result = (a - b) | (b - a)
print(len(result))
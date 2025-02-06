from sys import stdin


input = stdin.readline
n = int(input())

slope_set = set()

for _ in range(n):
    x, y = map(int, input().split())
    if y == 0:
        slope = "infinite"
    else:
        slope = y / x
    slope_set.add(slope)

print(len(slope_set))
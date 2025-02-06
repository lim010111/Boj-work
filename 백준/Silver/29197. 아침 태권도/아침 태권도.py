from sys import stdin


input = stdin.readline
n = int(input())

slope_dict = {}

for _ in range(n):
    x, y = map(int, input().split())

    if y == 0:
        slope_dict["infinite"] = True
        continue
    slope_dict[x / y] = True

print(len(slope_dict))
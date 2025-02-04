from sys import stdin

input = stdin.readline

n = int(input())

orders = {input().rstrip(): i for i in range(n)}
queue = [input().rstrip() for _ in range(n)]

overtaken = 0

for id in queue:
    flag = False

    for key in orders:
        if flag:
            orders[key] -= 1
        if key == id:
            flag = True

    if orders[id] > 0:
        overtaken += 1
        continue


print(overtaken)
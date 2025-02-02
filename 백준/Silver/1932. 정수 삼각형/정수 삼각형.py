from sys import stdin
input = stdin.readline

n = int(input())

triangle = [list(map(int, input().split())) for _ in range(n)]

dp_list = [triangle[0][0]]
next_dp_list = []

for line in range(n):
    if line == n - 1:
        break
    for i, num in enumerate(dp_list):
        if next_dp_list:
            if next_dp_list[i] < dp_list[i] + triangle[line + 1][i]:
                next_dp_list[i] = dp_list[i] + triangle[line + 1][i]
        else:
            next_dp_list.append(dp_list[i] + triangle[line + 1][i])
        next_dp_list.append(dp_list[i] + triangle[line + 1][i + 1])

    dp_list = next_dp_list[:]
    next_dp_list = []

print(max(dp_list))
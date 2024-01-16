n = int(input())
li = []
for i in range(n):
    li.append(tuple(map(int, input().split())))

li.sort(key=lambda x:(x[1], x[0]))

max_cnt = 1
selected = li[0]

for i in range(1, n):
    if li[i][0] >= selected[1]:
        max_cnt += 1
        selected = li[i]

print(max_cnt)
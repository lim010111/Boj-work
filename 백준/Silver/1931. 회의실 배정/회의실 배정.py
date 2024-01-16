n = int(input())
meetings = []
for i in range(n):
    meetings.append(tuple(map(int, input().split())))

meetings.sort(key=lambda x:(x[1], x[0]))

cnt = 1
selected = meetings[0] # 맨 앞의 회의를 변수에 저장

for i in range(1, n):
    if meetings[i][0] >= selected[1]: # 방금 끝난 회의의 시간보다 시작 시간이 크거나 같으면 개수에 추가
        cnt += 1
        selected = meetings[i]

print(cnt)
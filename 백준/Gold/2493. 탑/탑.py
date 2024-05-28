n = int(input())
towers = list(map(int, input().split())) # 탑의 높이 입력
answer = [0] * n # 수신한 탑의 인덱스를 저장할 리스트

stack = [] # 스택 초기화
for i in range(n):
    while stack and towers[stack[-1]] < towers[i]: # 스택이 비어있지 않고, 스택의 탑이 현재 탑보다 작다면
        stack.pop() # 스택에서 pop
    if stack: # 스택이 비어있지 않으면
        answer[i] = stack[-1] + 1 # 스택의 top에 저장된 탑의 인덱스를 저장
    stack.append(i) # 현재 탑의 인덱스를 스택에 push

print(*answer) # 리스트 출력

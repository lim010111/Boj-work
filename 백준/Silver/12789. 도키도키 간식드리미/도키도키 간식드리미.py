from collections import deque

n = int(input())
queue = deque(list(map(int, input().split())))

need = 1
stack = []
flag = 0
while queue:
    if stack and stack[-1] == need:
        need += 1
        stack.pop()
        continue

    popped = queue.popleft()
    if popped == need:
        need += 1
        continue

    stack.append(popped)

while stack:
    if need == stack.pop():
        need += 1

if need == n + 1:
    print("Nice")
else:
    print("Sad")
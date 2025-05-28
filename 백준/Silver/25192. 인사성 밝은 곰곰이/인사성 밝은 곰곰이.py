from sys import stdin


input = stdin.readline

n = int(input())
logs = []
log = None
for _ in range(n):
    input_string = input().rstrip()
    if input_string == 'ENTER':
        if log is not None:
            logs.append(log)
        log = set()
        continue
    
    log.add(input_string)

logs.append(log)

count = 0
for log in logs:
    count += len(log)

print(count)
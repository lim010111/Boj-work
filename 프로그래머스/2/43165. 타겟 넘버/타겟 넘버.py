from collections import deque

def solution(numbers, target):
    methods = 0
    queue = deque([(0, 0)])
    
    while queue:
        num, operation_counts = queue.popleft()
        for x in [-1, 1]:
            nxt_num = num + numbers[operation_counts] * x
            
            if operation_counts == len(numbers) - 1:
                if nxt_num == target:
                    methods += 1
                continue
                    
            queue.append((nxt_num, operation_counts + 1))
            
        

    return methods
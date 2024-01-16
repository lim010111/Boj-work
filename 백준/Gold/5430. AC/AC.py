import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    fs = input().rstrip()
    input()
    array = deque(input().rstrip()[1:-1].split(','))

    flag = 1
    
    if array[0] == "":
        array = deque([])

    back = ""
    direction = 1
    for i in range(len(fs)):
        if fs[i] == "R":
            direction *= -1
                
        elif fs[i] == "D":
            if direction == 1:
                try:
                    array.popleft()
                except:
                    print("error")
                    flag = 0
                    break
            else:
                try:
                    array.pop()
                except:
                    print("error")
                    flag = 0
                    break
        
        
    if flag:
        if direction == 1:
            print("["+",".join(array)+"]")
        else:
            array.reverse()
            print("["+",".join(array)+"]")
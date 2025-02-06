from sys import stdin


input = stdin.readline
n = int(input())

vector_set = set()

for _ in range(n):
    x, y = map(int, input().split())

    if y == 0 and x > 0:
        vector = (0, "right")
    elif y == 0 and x < 0:
        vector = (0, "left")
    elif x == 0 and y > 0:
        vector = (0, "top")
    elif x == 0 and y < 0:
        vector = (0, "bottom")
    else:
        if x > 0:
            if y > 0:
                q = 1
            else:
                q = 4
        else:
            if y > 0:
                q = 2
            else:
                q = 3
                
        vector = (q, y / x)

    vector_set.add(vector)
    

print(len(vector_set))
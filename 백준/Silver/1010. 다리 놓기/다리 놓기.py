t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    top = 1
    iter = n
    while iter:
        top *= m
        iter -= 1
        m -= 1
    bottom = 1
    for i in range(n, 0, -1):
        bottom *= i

    print(top // bottom)
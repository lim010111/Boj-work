import sys


def w(a, b, c):
    if (a, b, c) in memory:
        return memory[(a, b, c)]
        
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        memory[(a, b, c)] = w(20, 20, 20)
        return w(20, 20, 20)

    if a < b and b < c:
        memory[(a, b, c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

    else:
        memory[(a, b, c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)


if __name__ == "__main__":
    input_data = []
    memory = {}
    
    while True:
        a, b, c = map(int, sys.stdin.readline().split())
        if (a, b, c) == (-1, -1, -1):
            break
        input_data.append((a, b, c))

    for a, b, c in input_data:
        print(f"w({a}, {b}, {c}) = {w(a, b, c)}")
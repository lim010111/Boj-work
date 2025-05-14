def nth_fraction(n: int):

    i = 1
    while True:
        if n - i <= 0:
            break
        n -= i
        i += 1

    if i % 2 == 0:
        left, right = n, i - n + 1

    else:
        left, right = i - n + 1, n

    return f"{left}/{right}"


x = int(input())

print(nth_fraction(x))
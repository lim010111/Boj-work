def get_divisors(num):
    divisors = set()
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            divisors.add(i)
            divisors.add(num // i)

    return divisors


def get_gcd(a, b):
    a_divisors = get_divisors(a)
    b_divisors = get_divisors(b)
    gcd = max(a_divisors & b_divisors)

    return gcd


def get_gcm(a, b):
    gcd = get_gcd(a, b)
    gcm = (a // gcd) * (b // gcd) * gcd
    return gcm


a, b = map(int, input().split())
answer = get_gcm(a, b)
print(answer)
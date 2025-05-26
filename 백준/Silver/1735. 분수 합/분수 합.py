def get_gcd(a, b):
    a_divisor_set = set()
    for i in range(1, int(a**0.5) + 1):

        if a % i == 0:
            a_divisor_set.add(i)
            a_divisor_set.add(a // i)

    b_divisor_set = set()
    for i in range(1, int(b**0.5) + 1):
        if b % i == 0:
            b_divisor_set.add(i)
            b_divisor_set.add(b // i)

    gcd = max(a_divisor_set & b_divisor_set)
    return gcd


def get_irreducible_fraction(a, b, c, d):
    # b, d의 gcm 구하기

    gcd = get_gcd(b, d)
    gcm = b // gcd * d // gcd * gcd

    # 분모에 곱해지는 값을 분자에도 곱하기
    to_multiply_b = gcm // b
    to_multiply_d = gcm // d

    top = a * to_multiply_b + c * to_multiply_d
    bottom = gcm

    if get_gcd(top, bottom) >= 2:
        return f"{top//get_gcd(top, bottom)} {bottom//get_gcd(top, bottom)}"

    return f"{top} {bottom}"


a, b = map(int, input().split())
c, d = map(int, input().split())
answer = get_irreducible_fraction(a, b, c, d)
print(answer)
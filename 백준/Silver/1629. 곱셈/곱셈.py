def power(x, y, mod):
    if y == 0:
        return 1

    
    half = power(x, y // 2, mod) % mod

    if y % 2 == 0:
        return half * half % mod

    if y % 2 == 1:
        return x * half * half % mod
        
    

a, b, c = map(int, input().split())

print(power(a, b, c))
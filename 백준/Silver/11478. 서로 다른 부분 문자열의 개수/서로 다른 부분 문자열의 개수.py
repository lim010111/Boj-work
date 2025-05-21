s = input()
n = len(s)

partial_s = set()
for i in range(n):
    for j in range(0, n - i + 1):
        partial_s.add(s[j:j+i])

print(len(partial_s))
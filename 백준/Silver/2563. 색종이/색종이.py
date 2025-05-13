matrix = [[0] * 100 for _ in range(100)]

for _ in range(int(input())):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            matrix[x + i][y + j] = 1

total = 0
for i in range(100):
    total += sum(matrix[i])

print(total)
n = int(input())
array = list(map(int, input().split()))

stack = []
result = [-1] * n

for i in range(n):

    while stack and array[i] > array[stack[-1]]:
        result[stack[-1]] = array[i]
        stack.pop()

    stack.append(i)

print(" ".join(map(str, result)))
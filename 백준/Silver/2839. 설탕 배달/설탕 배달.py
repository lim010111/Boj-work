def min_bag(target: int):
    for i in range(0, 1000 + 1):
        for j in range(0, 4 + 1):
            if 5 * i + 3 * j == target:
                return i + j

    return -1


n = int(input())
print(min_bag(n))
def search(depth, order, length):
    if depth not in tree:
        tree[depth] = []
        
    tree[depth].append(order[length // 2])

    if length == 1:
        return
    search(depth + 1, order[:(length // 2)], length // 2)
    search(depth + 1, order[(length // 2) + 1:], length // 2)
    
    
k = int(input())

order = list(map(int, input().split()))

tree = {}
search(0, order, 2 ** k - 1)

for depth in tree:
    print(*tree[depth], sep=" ")
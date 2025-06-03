def dfs(start):
    if len(path) == m:
        print(*path)
        return

    for num in range(start, n + 1):
        path.append(num)
        dfs(num + 1)
        path.pop()
            

if __name__ == "__main__":
    n, m = map(int, input().split())
    path = []
    dfs(1)
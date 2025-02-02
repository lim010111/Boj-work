from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    n = int(input())

    stickers = [list(map(int, input().split())) for _ in range(2)]
    if n == 1:
        print(max((stickers[0][0], stickers[1][0])))

    else:
        dp = [[stickers[0][i], stickers[1][i]] for i in range(n)]

        dp[n - 2][0] += dp[n - 1][1]
        dp[n - 2][1] += dp[n - 1][0]

        for i in range(n - 3, -1, -1):
            dp[i][0] += max(dp[i + 1][1], dp[i + 2][1])
            dp[i][1] += max(dp[i + 1][0], dp[i + 2][0])

        print(max(dp[0][0], dp[0][1]))
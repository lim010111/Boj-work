def solve(n):
    # 1 ~ n까지의 n개의 dp 테이블, 0은 무시
    dp = [0] * (n + 1)


    dp[1] = 0
    # 2에서 시작해서 n까지, 순차적으로 최소 연산 횟수 구하기.
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)

        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

    return dp[n]
    


if __name__ == "__main__":
    n = int(input())
    answer = solve(n)
    print(answer)
def max_longest_subsequence(N, sequence):
    # dp: sequence[i]를 마지막 원소로 갖는 가장 큰 증가 부분수열
    dp = sequence[:]
    
    for i in range(1, N):
        # 직전 dp의 마지막 원소보다 seq[i]가 크다면, 증가 이어가기
        for j in range(i):
            if sequence[j] < sequence[i]:
                dp[i] = max(dp[i], dp[j] + sequence[i])

    return max(dp)


    

if __name__ == "__main__":
    N = int(input())
    sequence = list(map(int, input().split()))
    answer = max_longest_subsequence(N, sequence)
    print(answer)
def solution(n, k, nums):
    if n == k:
        return sum(nums)
    
    start, end = nums[0], nums[0 + k]

    partial_sum = [0] * (n - k + 1)
    partial_sum[0] = sum(nums[:k])
    for i in range(1, n - k + 1):
        start, end = nums[i - 1], nums[i - 1 + k]
        partial_sum[i] = partial_sum[i - 1] - start + end
    return max(partial_sum)
        
        

if __name__ == "__main__":
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    answer = solution(n, k, nums)
    print(answer)
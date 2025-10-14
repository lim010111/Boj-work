def solution(N):
    return "SK" if N % 2 == 1 else "CY"

if __name__ == "__main__":
    N = int(input())
    ans = solution(N)
    print(ans)
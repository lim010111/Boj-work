import sys
input = sys.stdin.readline


def solution(n: int) -> int:
    seq = [1, 1, 1, 2, 2]

    if n <= 5:
        return seq[n - 1]
    
    while n - 5 > 0:
        seq.append(seq[-1] + seq[-5])
        n -= 1

    return seq[-1]
    

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        answer = solution(n)
        print(answer)
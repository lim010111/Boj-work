def solution(n: int) -> int:
    x, y = 0, 1
    
    for _ in range(n - 1):
        x, y = y, x + y
    
    result = y % 1234567

    return result
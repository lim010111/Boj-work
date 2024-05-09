def solution(x: int) -> bool:
    if x % sum(list(map(int, list(str(x))))) == 0:
        return True
    else:
        return False
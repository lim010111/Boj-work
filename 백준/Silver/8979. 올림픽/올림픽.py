from typing import List, Tuple

def print_rank(info_list: List[Tuple[int]], k: int) -> int:
    info_list = sorted(info_list, key=lambda info:(-info[1], -info[2], -info[3]))


    if info_list[0][0] == k:
        return 1
        
    rank = 1
    for i in range(1, n):
        if info_list[i - 1][1:] != info_list[i][1:]:
            rank = i + 1
        if info_list[i][0] == k:
            return rank
        

if __name__ == "__main__":
    n, k = map(int, input().split())
    info_list = [tuple(map(int, input().split())) for _ in range(n)]
    result = print_rank(info_list, k)
    print(result)
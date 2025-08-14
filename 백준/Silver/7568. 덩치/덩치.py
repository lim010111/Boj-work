from typing import List, Tuple

def print_rank(info_list: List[Tuple[int, int]]) -> List[int]:
    ranking = []
    
    for i in range(n):
        x_weight, x_height = info_list[i]
        rank = 1
        for j in range(n):
            if i == j:
                continue
            y_weight, y_height = info_list[j]
            if x_weight < y_weight and x_height < y_height:
                rank += 1
        ranking.append(rank)

    return ranking
            

if __name__ == "__main__":
    n = int(input())
    info_list = [tuple(map(int, input().split())) for _ in range(n)] # (weight, height)

    result = print_rank(info_list)
    print(*result)
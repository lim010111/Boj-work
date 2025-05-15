from typing import List

def solution(sizes: List[List[int]]) -> int:
    answer = 0
    
    sorted_sizes = [sorted(size, reverse=True) for size in sizes]
    
    lefts = set()
    rights = set()
    for left, right in sorted_sizes:
        lefts.add(left)
        rights.add(right)
        
    answer = max(lefts) * max(rights)
        
    return answer
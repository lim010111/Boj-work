from typing import List


def solution(citations: List[int]) -> int:

    citations.sort(reverse=True)
    

    print(citations)
    for i, elem in enumerate(citations):
        print(i, elem)
        if i + 1 > elem:
            return i

        elif i == len(citations) - 1:
            return i + 1
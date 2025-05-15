from typing import List

def solution(answers: List[int]) -> List:
    answer = []

    n = len(answers)

    predicts = [[1, 2, 3, 4, 5] * (n // 5 + 1),
                [2, 1, 2, 3, 2, 4, 2, 5] * (n // 8 + 1),
                [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (n // 10 + 1)]

    man = {1:0, 2:0, 3:0}

    for i in range(n):
        for j in range(3):
            if predicts[j][i] == answers[i]:
                man[j + 1] += 1

    max_correct = max(man.values())
    answer = [m for m in man if man[m] == max_correct]

    return answer
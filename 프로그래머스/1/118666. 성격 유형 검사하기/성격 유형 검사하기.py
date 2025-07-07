def solution(survey, choices):
    score_dict = {
        "R": 0,
        "T": 0,
        "C": 0,
        "F": 0,
        "J": 0,
        "M": 0,
        "A": 0,
        "N": 0,
    }

    n = len(survey)
    
    
    for i in range(n):
        choice = choices[i]
        left, right = survey[i][0], survey[i][1]

        if choice < 4:
            score_dict[left] += 4 - choice

        elif choice > 4:
            score_dict[right] += choice - 4

    result = ""

    def decide_personality(kind):
        a, b = kind[0], kind[1]
        if score_dict[a] > score_dict[b]:
            return a

        if score_dict[a] < score_dict[b]:
            return b

        else:
            return a

    kinds = ["RT", "CF", "JM", "AN"]

    for kind in kinds:
        result += decide_personality(kind)

    return result
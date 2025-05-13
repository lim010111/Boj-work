from sys import stdin

input = stdin.readline


def mean_major_score() -> float:

    record_dict = {
        "A+": 4.5,
        "A0": 4.0,
        "B+": 3.5,
        "B0": 3.0,
        "C+": 2.5,
        "C0": 2.0,
        "D+": 1.5,
        "D0": 1.0,
        "F": 0.0,
    }

    total_score = 0
    scores = 0

    for _ in range(20):
        subject, score, record = input().rstrip().split()

        score = float(score)

        if record != "P":
            total_score += score * record_dict[record]
            scores += score

    return total_score / scores


print(f"{mean_major_score():.6f}")
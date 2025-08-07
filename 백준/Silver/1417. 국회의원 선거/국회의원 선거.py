def min_count():
    current_vote = {candidate:voted for candidate, voted in predicted_vote}

    current_sorted = sorted(current_vote.items(), key=lambda x:(-x[1], -x[0]))

    count = 0
    while current_sorted[0][0] != 1:
        max_voted = current_sorted[0][0]
        current_vote[max_voted] -= 1
        current_vote[1] += 1
        current_sorted = sorted(current_vote.items(), key=lambda x:(-x[1], -x[0]))
        count += 1

    print(count)

if __name__ == "__main__":
    candidates = int(input())
    predicted_vote = [(i + 1, int(input())) for i in range(candidates)]
    min_count()
from collections import Counter


def solution(word: str):
    if len(set(word)) == 1:
        return word[0]
    
    word_counter = Counter(word)
    sorted_counts = sorted(word_counter.values(), reverse=True)
    if sorted_counts[0] == sorted_counts[1]:
        return "?"
    
    return word_counter.most_common(1)[0][0]

if __name__ == "__main__":
    word = input().upper()
    print(solution(word))
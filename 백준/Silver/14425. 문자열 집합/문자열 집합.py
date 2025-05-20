from sys import stdin

input = stdin.readline


def count_words_in_set(n, m, word_set, test_words):
    cnt = 0
    for word in test_words:
        if word in word_set:
            cnt += 1

    return cnt


n, m = map(int, input().split())
word_set = set(input().rstrip() for _ in range(n))
test_words = [input().rstrip() for _ in range(m)] 

answer = count_words_in_set(n, m, word_set, test_words)

print(answer)
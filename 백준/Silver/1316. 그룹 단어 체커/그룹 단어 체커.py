from sys import stdin

input = stdin.readline


def is_group_word(word: str) -> bool:
    word_set = set()

    memory = None
    for char in word:
        if memory is not None:
            if memory != char and char in word_set:
                return False

        word_set.add(char)
        memory = char

    return True


count = 0
for _ in range(int(input())):
    word = input().rstrip()
    if is_group_word(word):
        count += 1

print(count)
def count_croatia_chars(word: str) -> int:
    count = 0

    index = 0
    while index < len(word):

        if word[index:index + 2] in croatia_chars:
            index += 2

        elif word[index:index + 3] in croatia_chars:
            index += 3

        else:
            index += 1

        count += 1

    return count


croatia_chars = set(['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='])

word = input()
print(count_croatia_chars(word))
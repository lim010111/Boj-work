def countSpecificString(n, m, s) -> int:
    i = 0
    count = 0
    pattern_count = 0
    while i < m:
        if s[i - 1 : i + 2] == "IOI":
            pattern_count += 1
            i += 2

            if pattern_count == n:
                count += 1
                pattern_count -= 1

        else:
            pattern_count = 0
            i += 1

    return count


n, m, s = int(input()), int(input()), input()
print(countSpecificString(n, m, s))
def classify(a, b, c):
    length_list = sorted([a, b, c])
    max_length = length_list.pop()

    if max_length >= sum(length_list):
        return "Invalid"

    if a == b == c:
        return "Equilateral"

    if a == b or b == c or c == a:
        return "Isosceles"

    else:
        return "Scalene"

if __name__ == "__main__":
    while True:
        a, b, c = map(int, input().split())
        if (a, b, c) == (0, 0, 0):
            break

        print(classify(a, b, c))
def solution(x):
    count_transform = 0
    while len(x) > 1:
        count_transform += 1
        x = str(sum(map(int, list(x))))

    if x in ('3', '6', '9'):
        print(count_transform, "YES", sep="\n")
    else:
        print(count_transform, "NO", sep="\n")
        

if __name__ == "__main__":
    x = input()
    solution(x)
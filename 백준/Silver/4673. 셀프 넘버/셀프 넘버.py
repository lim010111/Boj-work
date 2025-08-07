def print_self_numbers() -> None:
    numbers = set(range(1, 10000 + 1))
    # print(numbers)

    for num in range(1, 10000):
        d_num = num + sum(map(int, list(str(num))))
        numbers -= {d_num}
        
    print(*sorted(numbers), sep="\n")

if __name__ == "__main__":
    print_self_numbers()
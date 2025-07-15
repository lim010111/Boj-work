def solution(expresstion: str) -> int:
    """
    docstring:
    1. expresstion에 존재하는 모든 연산자(최대: +, -, *)의 우선순위 경우의 수 구하기
    2. 구한 경우의 수를 바탕으로 모든 연산 결과 구하기
    3. 모든 연산 결과에서 절댓값이 가장 큰 수 리턴
    """

    def make_case(case):
        if len(case) == len(operator_set):
            cases.append(case[:])
            return
        for operator in operator_set:
            if operator not in case:
                case.append(operator)
                make_case(case)
                case.pop()

    def operate(left, right, operator):
        # print(left, right)
        left, right = int(left), int(right)
        if operator == "-":
            return left - right

        if operator == "+":
            return left + right

        if operator == "*":
            return left * right

    operator_set = set(char for char in expresstion if not char.isnumeric())

    cases = []
    for operator in operator_set:
        make_case([operator])

    expresstion_list = []
    num = ""
    for char in expresstion:
        if char.isnumeric():
            num += char

        else:
            expresstion_list.append(num)
            expresstion_list.append(char)
            num = ""
    expresstion_list.append(num)

    results = []
    for case in cases:
        duplicated = expresstion_list[:]
        for operator in case:
            # print(operator)
            i = 0
            while i < len(duplicated):
                # print("순회", i, duplicated[i], duplicated)
                if duplicated[i] == operator:
                    # print("before", duplicated, i)
                    duplicated = (
                        duplicated[: i - 1]
                        + [
                            operate(
                                duplicated[i - 1],
                                duplicated[i + 1],
                                operator,
                            )
                        ]
                        + duplicated[i + 2 :]
                    )
                    # print("after", duplicated, i - 1)
                    i -= 1
                else:
                    i += 1
        results.append(abs(*duplicated))

    # print(max(results))

    return max(results)
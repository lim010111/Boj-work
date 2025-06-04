def make_operators(inputs):
    operators = []
    
    for i, input in enumerate(inputs):
        while input > 0:
            operators.append(i)
            input -= 1

    return operators


def dfs(case, used) -> None:
    if len(case) == len(operators):
        cases.append(case[:])
        return

    for i, operator in enumerate(operators):
        if not used[i]:
            case.append(operator)
            used[i] = True
            dfs(case, used)
            used[i] = False
            case.pop()

def find_max_min_cal(cases):
    results = set()
    for case in cases:
        result = nums[:]
        for i, operator_index in enumerate(case):
            if operator_index == 0:
                result[i + 1] = result[i] + result[i + 1]
            if operator_index == 1:
                result[i + 1] = result[i] - result[i + 1]
            if operator_index == 2:
                result[i + 1] = result[i] * result[i + 1]
            if operator_index == 3:
                if result[i + 1] == 0:
                    break
                if result[i] < 0:
                    result[i + 1] = -(-result[i] // result[i + 1])
                else:
                    result[i + 1] = result[i] // result[i + 1]

        results.add(result[-1])

    return max(results), min(results)


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    inputs = list(map(int, input().split())) # +, -, *, //
    operators = make_operators(inputs)
    cases = []
    dfs([], [False] * len(operators))
    cases = set([tuple(case) for case in cases])
    print(*find_max_min_cal(cases), sep="\n")
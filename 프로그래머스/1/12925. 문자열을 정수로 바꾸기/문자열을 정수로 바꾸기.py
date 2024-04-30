def solution(s: str) -> int:
    answer: int = 0

    if not s[0].isdigit():
        sign: str = s[0]
        number: int = int(s[1:])


        if sign == '-':
            number *= -1

        answer = number

    else:
        answer = int(s)

    return answer

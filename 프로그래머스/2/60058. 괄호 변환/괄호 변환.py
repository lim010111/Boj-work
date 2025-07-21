def solution(p: str) -> str:
    if p == "":
        return ""
    
    # 2. 두 균형잡힌 괄호 문자열로 분리
    closed, opened = 0, 0
    for char in p:
        if char == "(":
            opened += 1
        else:
            closed += 1
        if opened == closed:
            left, right = p[:opened + closed], p[opened + closed:]
            break

    # 3. left가 올바른 괄호 문자열이라면, right에 대해서 1단계부터 다시 수행
    vaildation_counter = 0
    for char in left:
        if char == "(":
            vaildation_counter += 1
        else:
            vaildation_counter -= 1
        
        if vaildation_counter < 0:
            # left를 올바른 괄호 문자열 만들기
            left_new = ""
            for char in left[1:-1]:
                if char == ")":
                    left_new += "("
                else:
                    left_new += ")"
            string = "(" + solution(right) + ")" + left_new
            return string
    
    return left + solution(right)
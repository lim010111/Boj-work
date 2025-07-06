def solution(new_id):
    '''
    1. 대문자 -> 소문자
    2. [소문자, 숫자, -, _, .] 제외 모든 문자 제거
    3. '.' 연속 불가능
    4. '.' 위치 맨 앞이나 뒤 불가능
    5. "" -> "a"
    6. 16자 이상이면 15자 남겨두고 제거, 제거 후 4번 규칙 적용
    7. 문자의 길이가 2 이하일 경우, 마지막 문자를 길이가 3이 될때까지 끝에 붙임. 
    '''

    chars = list(new_id.lower())

    for i, char in enumerate(chars):
        if not char.isalpha() and not char.isnumeric() and char != "-" and char != "_" and char !=".":
            chars[i] = ""

    chars = list("".join(chars))
    
    for i in range(len(chars)):
        if chars[i] == ".":
            for j in range(i+1, len(chars)):
                if chars[j] == ".":
                    chars[j] = ""
                else:
                    break
    
    string = "".join(chars)

    if string and string[0] == ".":
        string = string[1:]

    if string and string[-1] == ".":
        string = string[:-1]

    if string == "":
        string = "a"

    if len(string) >= 16:
        string = string[:15]

        if string[-1] == ".":
            string = string[:-1]

    if len(string) == 1:
        string += string[-1] + string[-1]

    if len(string) == 2:
        string += string[-1]

    return string
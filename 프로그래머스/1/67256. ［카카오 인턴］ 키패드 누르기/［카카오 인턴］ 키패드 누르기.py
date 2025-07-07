def solution(numbers, hand):
    '''
    [1 2 3]
    [4 5 6]
    [7 8 9]
    [* 0 #]

    현재 위치 -> (x, y)
    타겟 위치 -> (n, m)
    x, y - > n, m 까지의 거리 누가 더 작아?
    
    for num in nums:
        target = num
        if target in (1, 4, 7):
            왼손이동
        elif target in (3, 6, 9):
            오른손이동
        else:
            왼손 vs 오른손 거리

            if 동일하다면:
                어느손잡이?
    '''

    result = ""
    
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [-1, 0, -1],
    ]

    

    pos_left = (3, 0)
    pos_right = (3, 2)
    
    for number in numbers:
        if number in {1, 4, 7}:
            pos_left = (number//3, 0)
            result += "L"

        elif number in {3, 6, 9}:
            pos_right = (number//3 - 1, 2)
            result += "R"

        else:
            target = (number//3, 1) if number != 0 else (3, 1)
            d_left = abs(pos_left[0] - target[0]) + abs(pos_left[1] - target[1])
            d_right = abs(pos_right[0] - target[0]) + abs(pos_right[1] - target[1])
            # print(number, pos_left, pos_right, target)
            # print(d_left, d_right)
            if d_right > d_left:
                pos_left = target
                result += "L"

            elif d_left > d_right:
                pos_right = target
                result += "R"

            else:
                if hand == "left":
                    pos_left = target
                    result += "L"
                else:
                    pos_right = target
                    result += "R"

    return result
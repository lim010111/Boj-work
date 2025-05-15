from typing import List

def solution(numbers: List[int]) -> str:
    answer = ''
    
    # numbers_str = sorted(list(map(str, numbers)), key=lambda x: (-int(x[0]), -int(x[1]), -int(x[2]), -int(x[3])))
    str_nums = list(map(str, numbers))
    max_len = max(len(s) for s in str_nums)

    # s*max_len 을 키로, reverse=True 로 하면
    # '2'→'222', '11'→'111111', '101'→'101101101' 이 되고
    # lexicographical 내림차순 비교로도 원하는 정렬이 됩니다.
    numbers_str = sorted(str_nums, key=lambda s: s * max_len, reverse=True)

    
    answer = ''.join(numbers_str)
    
    if int(answer) == 0:
        return "0"
    
    return answer
from typing import List

def solution(mats: List[int], park: List[List[str]]) -> int:
    '''
    mats = [2, 3, 5] 라고 할때,
    for mat in mats:
        for i in range(0, len(park - mat))
            for j in range(0, len(park[i] - mat))
                if 돗자리 깔 수 있다면
                    mat를 후보에 넣으세요.
                    break
                    
    돗자리 깔 수 있는지 함수를 그냥 만들자.
    '''
    
    def is_available_mat(mat, r, c):
        for i in range(r, r + mat):
            for j in range(c, c + mat):
                if park[i][j] != "-1":
                    return False
                
        return True
    
    available_mats = []
    
    row, column = len(park), len(park[0])
    
    for mat in mats:
        for r in range(row - mat + 1):
            for c in range(column - mat + 1):
                if is_available_mat(mat, r, c):
                    available_mats.append(mat)
    if not available_mats:
        return -1
    
    return max(available_mats)
                    
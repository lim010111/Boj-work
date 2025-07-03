from typing import List

def solution(park: List[str], routes: List[str]) -> List[int]:
    '''
    시작 -> routes[0] .. [1] .. [2] -> 결과

    def move(pos, movement) -> end_pos:
    '''

    def move(pos: List[int], op: str, n: int) -> List[int]:
        x, y = pos
        dx, dy = x, y

        if op == "E":
            dy = y + n
            if dy >= r:
                return pos

            for i in range(y + 1, dy + 1):
                if park[x][i] == "X":
                    return pos

        elif op == "W":
            dy = y - n
            if dy < 0:
                return pos

            for i in range(dy, y):
                if park[x][i] == "X":
                    return pos

        elif op == "S":
            dx = x + n
            if dx >= c:
                return pos

            for i in range(x + 1, dx + 1):
                if park[i][y] == "X":
                    return pos

        else:
            dx = x - n
            if dx < 0:
                return pos

            for i in range(dx, x):
                if park[i][y] == "X":
                    return pos

        return [dx, dy]


    r, c = len(park), len(park[0])

    print(r, c)
    for i in range(r):
        for j in range(c):
            print(i, j)
            if park[i][j] == "S":
                pos = [i, j]

    for route in routes:
        op, n = route.split()
        pos = move(pos, op, int(n))

    return pos
from typing import List


# sol 3: flattening
def solution(rows: int, columns: int, queries: List[List[int]]) -> List[int]:

    def rotate(r1, c1, r2, c2):
        flattened = []

        for c in range(c1, c2):
            flattened.append(matrix[r1][c])

        for r in range(r1, r2):
            flattened.append(matrix[r][c2])

        for c in range(c2, c1, -1):
            flattened.append(matrix[r2][c])

        for r in range(r2, r1, -1):
            flattened.append(matrix[r][c1])

        flattened = [flattened[-1]] + flattened[:-1]

        len_c, len_r = c2 - c1 + 1, r2 - r1 + 1

        # print(flattened)

        i = 0
        for c in range(c1, c2):
            matrix[r1][c] = flattened[i]
            i += 1

        for r in range(r1, r2):
            matrix[r][c2] = flattened[i]
            i += 1

        for c in range(c2, c1, -1):
            matrix[r2][c] = flattened[i]
            i += 1

        for r in range(r2, r1, -1):
            matrix[r][c1] = flattened[i]
            i += 1

        min_list.append(min(flattened))

        # [print(matrix[i]) for i in range(rows)]

    matrix = [[c + r * columns for c in range(1, columns + 1)] for r in range(rows)]

    min_list = []
    for query in queries:
        r1, c1, r2, c2 = query
        rotate(r1 - 1, c1 - 1, r2 - 1, c2 - 1)

    return min_list

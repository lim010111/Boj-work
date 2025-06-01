def draw(x, y, n):
    if n == 1:
        draw_matrix[x][y] = "*"
        return

    for i in range(3):
        for j in range(3):
            if (i, j) == (1, 1):
                continue
            draw(x + i * n // 3, y + j * n // 3, n // 3)


if __name__ == "__main__":
    n = int(input())
    draw_matrix = [[' '] * n for _ in range(n)]
    draw(0, 0, n)
    for row in draw_matrix:
        print(''.join(row))
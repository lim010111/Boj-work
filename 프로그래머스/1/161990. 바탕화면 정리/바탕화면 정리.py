def solution(wallpaper):
    
    points = []
    for r in range(len(wallpaper)):
        for c in range(len(wallpaper[0])):
            if wallpaper[r][c] == "#":
                points.append((r, c))

    min_r, min_c, max_r, max_c = len(wallpaper) - 1, len(wallpaper[0]) - 1, 0, 0

    for r, c in points:
        if r < min_r:
            min_r = r

        if r > max_r:
            max_r = r

        if c < min_c:
            min_c = c

        if c > max_c:
            max_c = c

    return [min_r, min_c, max_r+1, max_c+1]
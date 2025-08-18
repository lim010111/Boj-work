def move(pos_k, pos_s, movements):
    col_map = {chr(i):i-65 for i in range(65, 65 + 8)}
    row_map = {f'{i}':8-i for i in range(1, 8 + 1)}
    movement_map = {
        'R': (0, 1),
        'L': (0, -1),
        'B': (1, 0),
        'T': (-1, 0),
        'RT' : (-1, 1),
        'LT' : (-1, -1),
        'RB' : (1, 1),
        'LB' : (1, -1),
    }

    kr, kc = row_map[pos_k[1]], col_map[pos_k[0]]
    sr, sc = row_map[pos_s[1]], col_map[pos_s[0]]

    for movement in movements:
        nr, nc = movement_map[movement]
        nxt_kr, nxt_kc = kr + nr, kc + nc
        if nxt_kr < 0 or nxt_kc < 0 or nxt_kr > 7 or nxt_kc > 7:
            continue
        if (nxt_kr, nxt_kc) == (sr, sc):
            nxt_sr, nxt_sc = sr + nr, sc + nc
            if nxt_sr < 0 or nxt_sc < 0 or nxt_sr > 7 or nxt_sc > 7:
                continue
            sr, sc = nxt_sr, nxt_sc
        kr, kc = nxt_kr, nxt_kc
            
    
    end_pos_k = f"{chr(kc+65)}{8-kr}"
    end_pos_s = f"{chr(sc+65)}{8-sr}"
    
    return end_pos_k, end_pos_s

if __name__ == "__main__":
    pos_k, pos_s, n = input().split()
    n = int(n)
    movements = [input() for _ in range(n)]
    pos_k, pos_s = move(pos_k, pos_s, movements)
    print(pos_k, pos_s, sep="\n")
def solution(name):
    count = 0
    n = len(name)

    for i in range(n):
        distance = ord(name[i]) - ord('A')
        if distance > 13:
            distance = 26 - distance

        count += distance
        
    if count == 0:
        return 0

    min_move = n - 1
    for i in range(n):
        if name[i] == 'A':
            continue

        next = i + 1
        while next < n and name[next] == 'A':
            next += 1
                        
        right_and_left_move = i * 2 + (n - next)
        left_and_right_move = (n - next) * 2 + i
        min_move = min(min_move, right_and_left_move, left_and_right_move)

    count += min_move
    
    return count
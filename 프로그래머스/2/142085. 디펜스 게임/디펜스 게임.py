import heapq

def solution(n, k, enemy):

    remain = n
    make_invincible = k

    attacked_enemy = []
    heapq.heapify(attacked_enemy)

    count = 0

    for e in enemy:
        remain -= e
        heapq.heappush(attacked_enemy, -e)

        if remain < 0:
            if make_invincible == 0:
                return count

            make_invincible -= 1
            max_attacked = -heapq.heappop(attacked_enemy)
            remain = remain + max_attacked if remain + max_attacked <= n else n

        count += 1

    return count
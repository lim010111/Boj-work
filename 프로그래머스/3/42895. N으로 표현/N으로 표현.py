from collections import deque

def solution(N, number):
    target = number

    len_limit_number = len(str(target * N))
    init_nums = [int(str(N) * len) for len in range(1, len_limit_number + 1)]
    queue = deque(init_nums)

    # dict: {사용된 숫자: N 사용 횟수}
    used_number = {num: len(str(num)) for num in queue}

    print(queue)
    while queue:
        cur_num = queue.popleft()
        if used_number[cur_num] == 8:
            continue

        if cur_num == target:
            return used_number[cur_num]

        try:
            for init_num in init_nums:
                for nxt_num in [
                    cur_num + init_num,
                    cur_num - init_num,
                    cur_num * init_num,
                    cur_num // init_num,
                    init_num // cur_num,
                    init_num - cur_num,
                    ]:
                    for sign in [-1, -1]:
                        nxt_num *= sign

                        if nxt_num > 32000 or nxt_num < -N:
                            continue


                        if nxt_num not in used_number:
                            used_number[nxt_num] = used_number[cur_num] + len(str(init_num))
                            if nxt_num == target:
                                if any(
                                    used_number[nxt_num] - 1 > used_number[num] for num in queue
                                ):
                                    continue
                                return used_number[nxt_num] if used_number[nxt_num] <= 8 else -1
                            queue.append(nxt_num)

                        else:
                            used_number[nxt_num] = min(
                                used_number[nxt_num], used_number[cur_num] + len(str(init_num))
                            )

        except ZeroDivisionError:
            pass
        
        try:
            for init_num in init_nums:
                for nxt_num in [
                    cur_num + (init_num // N),
                    cur_num - (init_num // N),
                    cur_num * (init_num // N),
                    cur_num // (init_num // N),
                    (init_num // N) // cur_num,
                    (init_num // N) - cur_num,
                    ]:
                    for sign in [-1, -1]:
                            nxt_num *= sign

                            if nxt_num > 32000 or nxt_num < -N:
                                continue


                            if nxt_num not in used_number:
                                used_number[nxt_num] = used_number[cur_num] + len(str(init_num)) + 1
                                if nxt_num == target:
                                    if any(
                                        used_number[nxt_num] - 1 > used_number[num] for num in queue
                                    ):
                                        continue
                                    return used_number[nxt_num] if used_number[nxt_num] <= 8 else -1
                                queue.append(nxt_num)

                            else:
                                used_number[nxt_num] = min(
                                    used_number[nxt_num], used_number[cur_num] + len(str(init_num)) + 1
                                )
        except ZeroDivisionError:
            pass
                    
    return used_number[target] if used_number[target] <= 8 else -1
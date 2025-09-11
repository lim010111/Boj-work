from collections import deque

def solution(N, number):
    init_nums = {int(str(N) * i):i for i in range(1, len(str(number * N)) + 1)}

    queue = deque(init_nums.keys())

    cost_dict = {key:value for key,value in init_nums.items()}

    while queue:
        cur_num = queue.popleft()

        for init_num, cost in init_nums.items():

            # 다음 연산이 cost를 넘기게 되면 탈출
            if cost_dict[cur_num] + cost > 8:
                break

            try:
                next_nums = [
                    cur_num + init_num,
                    cur_num - init_num,
                    cur_num * init_num,
                    cur_num // init_num,
                    init_num - cur_num,
                    init_num // cur_num,
                ]
                for next_num in next_nums:
                    if next_num not in cost_dict:
                        cost_dict[next_num] = cost_dict[cur_num] + cost
                        queue.append(next_num)
                    
                    else:
                        cost_dict[next_num] = min(
                            cost_dict[next_num], cost_dict[cur_num] + cost
                        )

            except ZeroDivisionError:
                pass
    if number in cost_dict:
        return cost_dict[number]
    else: 
        return -1 
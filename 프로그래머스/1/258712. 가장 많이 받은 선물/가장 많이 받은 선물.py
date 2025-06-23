from typing import List


def solution(friends: List[str], gifts: List[str]) -> int:
    answer = 0

    give_info = {friend: {f: 0 for f in friends} for friend in friends}

    received_info = {friend: 0 for friend in friends}

    # 이번 달 교환 통계 딕셔너리
    for gift in gifts:
        g, r = gift.split()
        # if r not in give_info[g]:
        #     give_info[g][r] = 0
        give_info[g][r] += 1
        received_info[r] += 1

    next_month_info = {friend: 0 for friend in friends}

    # 다음 달 받을 선물 순차적으로 확인
    for i in range(len(friends)):
        a = friends[i]
        for j in range(i + 1, len(friends)):
            b = friends[j]

            # 저번 달에 누가 더 많이 줬어?
            if give_info[a][b] > give_info[b][a]:
                next_month_info[a] += 1

            elif give_info[a][b] < give_info[b][a]:
                next_month_info[b] += 1

            else:
                # 선물 지수 비교
                a_score = sum(give_info[a].values()) - received_info[a]
                b_score = sum(give_info[b].values()) - received_info[b]
                if a_score > b_score:
                    next_month_info[a] += 1

                elif a_score < b_score:
                    next_month_info[b] += 1

    answer = max(next_month_info.values())

    return answer

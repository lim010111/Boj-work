from typing import List


def solution(genres: List[str], plays: List[int]) -> List[int]:
    datas = {}
    total_play_datas = {}

    result = []

    for i in range(len(genres)):

        genre = genres[i]
        play = plays[i]

        if genre not in datas:
            datas[genre] = []
            total_play_datas[genre] = 0

        datas[genre].append((play, i))
        total_play_datas[genre] += play

    for genre in datas:
        datas[genre].sort(
            key=lambda x: (-x[0], x[1]))

    sorted_genres = sorted(total_play_datas.keys(),
                           key=lambda x: -total_play_datas[x])


    for genre in sorted_genres:
        result.append(datas[genre][0][1])

        try:
            result.append(datas[genre][1][1])
        except IndexError:
            pass

    return result
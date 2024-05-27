from typing import List


def solution(participant: List[str], completion: List[str]) -> str:
    participant_dict = {}
    completion_dict = {}

    for elem in participant:
        if elem not in participant_dict:
            participant_dict[elem] = 1
        else:
            participant_dict[elem] += 1

    for elem in completion:
        if elem not in completion_dict:
            completion_dict[elem] = 1
        else:
            completion_dict[elem] += 1


    for key in participant_dict:
        if key not in completion_dict:
            return key

        if participant_dict[key] != completion_dict[key]:
            return key
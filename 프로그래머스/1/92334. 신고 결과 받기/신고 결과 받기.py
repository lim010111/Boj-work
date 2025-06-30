from typing import Dict, Any

def solution(id_list, report, k):
    result = [0] * len(id_list)
    report = list(set(report))
    banned = set()
    info: Dict[str, Dict[str, Any]] = {id:{'index': i, 'report': set(), 'reported': 0} for i, id in enumerate(id_list)}

    for report_info in report:
        give, given = report_info.split(" ")
        info[give]['report'].add(given)
        info[given]['reported'] += 1
        if info[given]['reported'] == k:
            banned.add(given)

    for id in info:
        result[info[id]['index']] = len(info[id]['report'] & banned)

    return result

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

ans = solution(id_list, report, k)
print(ans)
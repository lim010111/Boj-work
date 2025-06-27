from typing import List

def total_time(m, s):
    return int(m) * 60 + int(s)

def next(time: str, video_len) -> str:
    cur_m, cur_s = map(int, time.split(':'))
    cur_s += 10
    if cur_s >= 60:
        cur_s -= 60
        cur_m += 1

    if total_time(cur_m, cur_s) >= total_time(*list(map(int, video_len.split(':')))):
        return video_len

    return f"{cur_m:02d}:{cur_s:02d}"

def prev(time: str) -> str:
    cur_m, cur_s = map(int, time.split(':'))
    cur_s -= 10
    if cur_s < 0:
        cur_s += 60
        cur_m -= 1

    if total_time(cur_m, cur_s) <= 0:
        return f"00:00"

    return f"{cur_m:02d}:{cur_s:02d}"

def skip_op(time: str, op_start: str, op_end: str) -> str:
    cur_m, cur_s = map(int, time.split(':'))
    start_m, start_s = map(int, op_start.split(':'))
    end_m, end_s = map(int, op_end.split(':'))
        
    if total_time(start_m, start_s) <= total_time(cur_m, cur_s) <= total_time(end_m, end_s):
        return op_end
    
    
    return time

def solution(video_len: str, pos: str, op_start: str, op_end: str, commands: List[str]) -> str:

    for cmd in commands:
        pos = skip_op(pos, op_start, op_end)
        print(pos)
        
        if cmd == "next":
            pos = next(pos, video_len)

        else:
            pos = prev(pos)

        print(pos)

        pos = skip_op(pos, op_start, op_end)

    return pos
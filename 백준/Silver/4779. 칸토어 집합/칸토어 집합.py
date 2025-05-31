import sys


def solution(start, end):
    if (end - start) <= 1:
        return 
    mid_index = start + (end - start + 1) // 3
    
    for i in range(mid_index, mid_index + (end - start + 1) // 3):
        line[i] = ' '
    solution(start, mid_index - 1)
    solution(mid_index + (end - start + 1) // 3, end)

if __name__ == "__main__":
    inputs = [int(data.rstrip()) for data in sys.stdin.readlines()]
    
    for input in inputs:
        line = list('-' * (3 ** input))
        answer = solution(0, 3 ** input - 1)
        print(''.join(line))
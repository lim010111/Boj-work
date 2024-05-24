from typing import List


def solution(array: List, commands: List[List]) -> List:
    results = []
    
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]

        if i == j:
            result = array[i-1]
        
        else:
            result = sorted(array[i-1:j])[k-1]

        results.append(result)


    return results
from typing import List, Dict
from collections import deque


def solution(begin: str, target: str, words: List[str]) -> int:
    visited: Dict[str, bool] = {word:False for word in words}

    queue = deque([(begin, 0)])
    length = len(target)

    while queue:
        word, count = queue.popleft()
        print(word)

        for next_word in words:
            if visited[next_word]:
                continue

            diff = 0
            for i in range(length):
                if next_word[i] != word[i]:
                    diff += 1

            if diff != 1:
                continue

            if next_word == target:
                return count + 1
                
            queue.append((next_word, count + 1))
            visited[next_word] = True

    return 0
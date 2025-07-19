# 프로그래머스: 무인도 여행
# https://school.programmers.co.kr/learn/courses/30/lessons/154540

from typing import List
from collections import deque

def solution(maps: List[str]) -> List[int]:
    [print(m) for m in maps]
    
    def bfs(r, c):
        foods: int = int(maps[r][c])
        visited[r][c] = True
        print(foods)
        movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        queue = deque([(r, c)])
        while queue:
            r, c = queue.popleft()
            
            for movement in movements:
                nr = r + movement[0]
                nc = c + movement[1]
                
                
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue
            
                if visited[nr][nc]:
                    continue
                
                if maps[nr][nc] == "X":
                    continue
                
                print(maps[nr][nc], foods)
                visited[nr][nc] = True
                foods += int(maps[nr][nc])
                queue.append((nr, nc))
        
        return foods
    results = []
    
    rows, cols = len(maps), len(maps[0])
    visited = [[False] * cols for _ in range(rows)]


    for r in range(rows):
        for c in range(cols):
            if maps[r][c] == "X" or visited[r][c] == True:
                continue
            print("진입")
            results.append(bfs(r, c))
            
    if not results:
        results.append(-1)

    return sorted(results)
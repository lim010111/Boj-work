from typing import List
from collections import deque

def solution(maps) -> List[int]:
    
    def bfs(r, c):
        foods = maps[r][c]
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
                
                if maps[nr][nc] == 0:
                    continue

                visited[nr][nc] = True
                foods += maps[nr][nc]
                queue.append((nr, nc))
        
        return foods
    results = []
    maps = [[int(char) if char.isnumeric() else 0 for char in m] for m in maps]
    print(maps)


    rows, cols = len(maps), len(maps[0])
    visited = [[False] * cols for _ in range(rows)]


    for r in range(rows):
        for c in range(cols):
            if maps[r][c] == 0:
                continue
            
            results.append(bfs(r, c))

    return results
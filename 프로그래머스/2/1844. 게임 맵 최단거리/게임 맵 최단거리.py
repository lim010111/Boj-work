from typing import List
from collections import deque

def solution(maps: List[List[int]]) -> int:
    answer = 0
    
    n, m = len(maps), len(maps[0])
    
    visited = [[False] * m for _ in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    queue = deque([(0, 0)])
    visited[0][0] = True
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
                continue
            
            if visited[nx][ny]:
                continue
                
            if maps[nx][ny] == 0:
                continue
                
            queue.append((nx, ny))
            maps[nx][ny] = maps[x][y] + 1
            visited[nx][ny] = True
            
        if maps[-1][-1] == 1:
            answer = -1
        else:
            answer = maps[-1][-1]
    
    return answer
from collections import deque
from sys import stdin
input = stdin.readline

def bfs(start_i, start_j, grid, r, c):
    # 방문 배열은 -1로 초기화 (방문하지 않은 상태)
    visited = [[-1] * c for _ in range(r)]
    q = deque()
    q.append((start_i, start_j))
    visited[start_i][start_j] = 0
    max_distance = 0
    
    while q:
        i, j = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + dx, j + dy
            if 0 <= ni < r and 0 <= nj < c:
                if grid[ni][nj] == 'L' and visited[ni][nj] == -1:
                    visited[ni][nj] = visited[i][j] + 1
                    max_distance = max(max_distance, visited[ni][nj])
                    q.append((ni, nj))
    return max_distance

def main():
    r, c = map(int, input().split())
    grid = [list(input().strip()) for _ in range(r)]
    
    answer = 0
    # 모든 육지 셀에서 BFS를 수행하여 최장 최단 거리를 갱신
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 'L':
                answer = max(answer, bfs(i, j, grid, r, c))
    print(answer)

if __name__ == '__main__':
    main()

import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y, z):
    q = deque([(x, y)])
    visit[x][y] = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny] and graph[nx][ny] > z:
                visit[nx][ny] = 1
                q.append((nx, ny))

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

max_rain = max(max(row) for row in graph)

res = 0
for water_level in range(max_rain):
    visit = [[0] * n for _ in range(n)]
    cnt = 0
    
    for j in range(n):
        for k in range(n):
            if graph[j][k] > water_level and not visit[j][k]:
                bfs(j, k, water_level)
                cnt += 1
    res = max(res, cnt)

print(res)

import sys
input = sys.stdin.readline
from collections import deque

dx,dy = [1,-1,0,0],[0,0,1,-1]

def sol(a,b):
    q = deque()
    q.append([a,b])
    visit[a][b] = True
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = dx[i]+x,dy[i]+y
            if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:
                if graph[nx][ny] != 0:
                    visit[nx][ny] = True
                    q.append([nx,ny])
                else:
                    sea[x][y] += 1
    return 1

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
y = 0

while True:
    ans = []
    visit = [[False]*m for _ in range(n)]
    sea = [[0]*m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and not visit[i][j]:
                ans.append(sol(i,j))
                
    for i in range(n):
        for j in range(m):
            graph[i][j] -= sea[i][j]
            if graph[i][j] < 0:
                graph[i][j] = 0
    if len(ans) == 0 or len(ans) >= 2:
        break
    y += 1
print(y) if len(ans) >= 2 else print(0)
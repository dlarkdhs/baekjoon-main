import sys
input = sys.stdin.readline
from collections import deque

def sol(a,b):
    dx,dy = [0,0,1,-1],[1,-1,0,0]
    q = deque()
    q.append([a,b])
    graph[a][b] = 0
    cnt = 1
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = dx[i]+x,dy[i]+y
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                q.append([nx,ny])
                graph[nx][ny] = 0
                cnt += 1
    return cnt

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

res = 0
mx = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            res += 1
            mx = max(sol(i,j),mx)
print(res)
print(mx)
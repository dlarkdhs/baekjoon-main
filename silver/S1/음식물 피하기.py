import sys
input = sys.stdin.readline
from collections import deque

dx,dy = [0,0,-1,1], [-1,1,0,0]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    graph[x][y] = 2
    
    cnt = 1
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx,ny = a+dx[i], b+dy[i]
            if 0 < nx <= n and 0 < ny <= m and graph[nx][ny] == 1:
                q.append((nx,ny))
                graph[nx][ny] = 2
                cnt += 1
    return cnt

n,m,k = map(int,input().split())
graph = [[0]*(m+1) for _ in range(n+1)]
ans = 0

for _ in range(k):
    a,b = map(int,input().split())
    graph[a][b] = 1

for i in range(1,n+1):
    for j in range(1,m+1):
        if graph[i][j] == 1:
            A = bfs(i,j)
            ans = max(A,ans)
print(ans)
import sys
input = sys.stdin.readline
from collections import deque

dx,dy = [1,-1,0,0],[0,0,1,-1]

def sol(x,y):
    q = deque()
    q.append([x,y])
    graph[x][y] = 1
    
    cnt = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = dx[i]+x,dy[i]+y
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                q.append([nx,ny])
                cnt += 1
    return cnt

n,m,k = map(int,input().split())
graph = [[0]*m for _ in range(n)]

for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(n-y2,n-y1):
        for j in range(x1,x2):
            graph[i][j] = 1

ans = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            ans.append(sol(i,j))
ans.sort()

print(len(ans))
print(*ans)
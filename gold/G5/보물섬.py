import sys
from collections import deque
input = sys.stdin.readline

global ans
ans = 0

dx,dy = [-1,1,0,0], [0,0,-1,1]

def bfs(x,y):
    global ans
    q = deque()
    q.append((x,y))
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx,ny = dx[i]+x, dy[i]+y
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[x][y] == "W":
                continue
            if graph[nx][ny] == "L" and d[nx][ny] == -1:
                d[nx][ny] = d[x][y]+1
                q.append((nx,ny))
                ans = max(d[nx][ny], ans)
    return ans

n,m = map(int,input().rstrip().split())
graph = []
for _ in range(n):
    graph.append(list(input().rstrip()))

for i in range(n):
    for j in range(m):
        if graph[i][j] == "L":
            d = [[-1] * m for _ in range(n)]
            d[i][j] = 0
            bfs(i,j)
print(ans)
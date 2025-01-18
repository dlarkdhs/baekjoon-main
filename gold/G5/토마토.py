import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(m)]
q = deque([])
dx,dy = [-1,1,0,0], [0,0,-1,1]
cnt = 0

for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            q.append([i,j])

def bfs():
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = dx[i]+x, dy[i]+y
            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]+1
                q.append([nx,ny])

bfs()
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    cnt = max(cnt,max(i))
print(cnt-1)
import sys
input = sys.stdin.readline
from collections import deque

dx,dy = [0,0,1,-1], [1,-1,0,0]

def bfs(graph,a,b):
    n = len(graph)
    q = deque()
    q.append((a,b))
    graph[a][b] = 0
    cnt = 1
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = dx[i]+x, dy[i]+y
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx,ny))
                cnt += 1
    return cnt

n = int(input())
graph = [list(map(int,input().rstrip())) for _ in range(n)]

c = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            c.append(bfs(graph,i,j))
c.sort()
print(len(c))
for i in c:
    print(i)
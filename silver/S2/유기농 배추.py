import sys
from collections import deque
input = sys.stdin.readline

dx,dy = [0,0,-1,1], [-1,1,0,0]

def bfs(graph,x,y):
    q = deque()
    q.append((x,y))
    graph[x][y] = 0
    
    while q:
        a,b = q.popleft()
        for i in range(4):
            na,nb = dx[i]+a, dy[i]+b
            if na < 0 or nb < 0 or na >= n or nb >= m:
                continue
            if graph[na][nb] == 1:
                graph[na][nb] = 0
                q.append((na,nb))
    return

t = int(input())
for _ in range(t):
    n,m,k = map(int,input().split())
    graph = [[0]*m for _ in range(n)]
    for _ in range(k):
        x,y = map(int,input().split())
        graph[x][y] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(graph,i,j)
                cnt += 1
    print(cnt)
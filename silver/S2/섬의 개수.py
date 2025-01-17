import sys
from collections import deque
input = sys.stdin.readline

dx,dy = [1,1,-1,-1,1,-1,0,0], [0,1,0,1,-1,-1,1,-1]

def dfs(a,b):
    q = deque()
    q.append((a,b))
    graph[a][b] = 0
    
    while q:
        x,y = q.popleft()
        for i in range(8):
            nx,ny = x+dx[i], y+dy[i]
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx,ny))

while True:
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        break
    
    graph = list(list(map(int,input().split())) for _ in range(h))
    
    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i,j)
                cnt += 1
    print(cnt)
                
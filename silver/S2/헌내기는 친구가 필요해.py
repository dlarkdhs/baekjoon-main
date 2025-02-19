import sys
input = sys.stdin.readline
from collections import deque

dx,dy = [0,0,1,-1],[1,-1,0,0]

def sol(x,y):
    global cnt
    q = deque()
    q.append([x,y])
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != "X":
                if graph[nx][ny] == "P":
                    cnt += 1
                graph[nx][ny] = "X"
                q.append([nx,ny])
    return cnt


n,m  = map(int,input().split())
graph = [list(input().rstrip()) for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == "I":
            res = sol(i,j)
if res == 0:
    print("TT")
else:
    print(res)
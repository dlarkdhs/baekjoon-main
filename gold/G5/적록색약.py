import sys
input = sys.stdin.readline
from collections import deque

dx,dy = [0,0,1,-1],[1,-1,0,0]

def sol(x,y):
    q = deque()
    q.append([x,y])
    visit[x][y] = 1
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = dx[i]+x,dy[i]+y
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0 and graph[nx][ny] == graph[x][y]:
                visit[nx][ny] = 1
                q.append([nx,ny])
            
n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
visit = [[0]*n for _ in range(n)]

res1,res2 = 0,0
for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            sol(i,j)
            res1 += 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == "G":
            graph[i][j] = "R"

visit = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            sol(i,j)
            res2 += 1
print(res1,res2)
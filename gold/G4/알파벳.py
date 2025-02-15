import sys
input = sys.stdin.readline

dx,dy = [1,-1,0,0],[0,0,1,-1]

def sol(x,y):
    alp = ord(graph[x][y])-65
    global cnt
    cnt = max(cnt,visit[alp])
    
    for i in range(4):
        nx,ny = dx[i]+x,dy[i]+y
        if 0 <= nx < r and 0 <= ny < c:
            a = ord(graph[nx][ny])-65
            if not visit[a]:
                visit[a] = visit[alp]+1
                sol(nx,ny)
                visit[a] = 0

r,c = map(int,input().split())
graph = [list(input().rstrip()) for _ in range(r)]
visit = [0]*26

cnt = 0
alp = ord(graph[0][0])-65
visit[alp] = 1
sol(0,0)
print(cnt)
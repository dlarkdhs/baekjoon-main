import sys
input = sys.stdin.readline

dx,dy = [0,0,1,-1],[1,-1,0,0]

r,c,k = map(int,input().split())
graph = [list(input().rstrip()) for _ in range(r)]
ans = 0

def bfs(x,y,cnt):
    global ans
    
    if cnt == k and x == 0 and y == c-1:
        ans += 1
    else:
        graph[x][y] = 'T'
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] == '.':
                graph[nx][ny] = 'T'
                bfs(nx,ny,cnt+1)
                graph[nx][ny] = '.'
bfs(r-1,0,1)
print(ans)
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
cnt = 0

graph = [[]*n for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visit = [0]*(n+1)
def dfs(v):
    global cnt
    visit[v] = 1
    for i in graph[v]:
        if visit[i] == 0:
            dfs(i)
            cnt += 1
dfs(1)
print(cnt)
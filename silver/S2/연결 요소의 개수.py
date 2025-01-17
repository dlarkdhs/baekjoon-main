import sys
input = sys.stdin.readline
from collections import deque

def dfs(graph, x, visit):
    visit[x] = True
    for i in graph[x]:
        if not visit[i]:
            dfs(graph, i, visit)

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
visit = [False] * (n+1)
for i in range(1,n+1):
    if not visit[i]:
        dfs(graph, i, visit)
        cnt += 1
print(cnt)
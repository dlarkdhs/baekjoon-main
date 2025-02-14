import sys
input = sys.stdin.readline
from collections import deque

cnt = 1
def bfs(x):
    global cnt
    q = deque([x])
    visit[x] = cnt
    while q:
        n = q.popleft()
        for i in graph[n]:
            if visit[i] == 0:
                cnt += 1
                visit[i] = cnt
                q.append(i)

n,m,r = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visit = [0]*(n+1)

for i in range(n+1):
    graph[i].sort()

bfs(r)
for i in range(1,n+1):
    print(visit[i])
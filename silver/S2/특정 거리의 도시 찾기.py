import sys
input = sys.stdin.readline
from collections import deque

n,m,k,x = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
visit = [-1]*(n+1)

q = deque()
q.append(x)
visit[x] = 0
while q:
    N = q.popleft()
    for i in graph[N]:
        if visit[i] == -1:
            visit[i] = visit[N]+1
            q.append(i)

if k in visit:
    for i in range(1,n+1):
        if visit[i] == k:
            print(i)
else:
    print(-1)
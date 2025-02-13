import sys
input = sys.stdin.readline
from collections import deque

def sol(x):
    q = deque([x])
    visit[x] = 1
    
    while q:
        n = q.popleft()
        for i in graph[n]:
            if not visit[i]:
                visit[i] = visit[n]+1
                q.append(i)

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

res = []
for i in range(1,n+1):
    visit = [0]*(n+1)
    sol(i)
    res.append(sum(visit))
print(res.index(min(res))+1)
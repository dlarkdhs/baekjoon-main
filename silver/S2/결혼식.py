import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visit = [0 for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(x):
    q = deque()
    q.append(x)
    visit[x] = 1
    
    while q:
        a = q.popleft()
        for i in graph[a]:
            if visit[i] == 0:
                q.append(i)
                visit[i] = visit[a]+1
bfs(1)
res = 0
for i in range(2,n+1):
    if visit[i] < 4 and visit[i] != 0:
        res += 1
print(res)
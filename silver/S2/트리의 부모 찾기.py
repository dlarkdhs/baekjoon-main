import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visit = [0]*(n+1)

def sol(x):
    q = deque([x])
    while q:
        n = q.popleft()
        for i in graph[n]:
            if visit[i] == 0:
                visit[i] = n
                q.append(i)

sol(1)
for i in range(2,n+1):
    print(visit[i])
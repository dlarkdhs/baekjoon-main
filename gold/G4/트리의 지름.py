import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def sol(x,y):
    for i,r in graph[x]:
        if visit[i] == -1:
            visit[i] = y+r
            sol(i,y+r)

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,r = map(int,input().split())
    graph[a].append((b,r))
    graph[b].append((a,r))

visit = [-1]*(n+1)
visit[1] = 0
sol(1,0)

res = visit.index(max(visit))
visit = [-1]*(n+1)
visit[res] = 0
sol(res,0)
print(max(visit))
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(v):
    global cur
    ans[v] = cur
    cur += 1
    for next_v in graph[v]:
        if ans[next_v] == 0:
            dfs(next_v)

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
ans = [0] * (n + 1)
cur = 1

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    graph[i].sort(reverse=True)

dfs(r)
for i in range(1, n + 1):
    print(ans[i])
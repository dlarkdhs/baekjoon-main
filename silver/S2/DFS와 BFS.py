import sys
input = sys.stdin.readline

n,m,v = map(int,input().split())

graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1

visit1 = [0]*(n+1)
visit2 = [0]*(n+1)

def dfs(v):
    visit1[v] = 1
    print(v, end=" ")
    for i in range(1,n+1):
        if graph[v][i] == 1 and visit1[i] == 0:
            dfs(i)

def bfs(v):
    queue = [v]
    visit2[v] = 1
    while queue:
        v = queue.pop(0)
        print(v, end=" ")
        for i in range(1,n+1):
            if visit2[i] == 0 and graph[v][i] == 1:
                queue.append(i)
                visit2[i] = 1

dfs(v)
print()
bfs(v)
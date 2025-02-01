import sys
input = sys.stdin.readline
        
n = int(input())
x,y = map(int,input().split())
graph = [[] for _ in range(n+1)]
m = int(input())

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visit = [False]*(n+1)
res = []

def dfs(a,num):
    global flag
    visit[a] = True
    
    if a == y:
        flag = True
        print(num)
    
    for i in graph[a]:
        if not visit[i]:
            dfs(i,num+1)

flag = False
dfs(x,0)
if not flag:
    print(-1)
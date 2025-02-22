import sys
input = sys.stdin.readline
from collections import deque
    

k = int(input())
for _ in range(k):
    v,e = map(int,input().split())
    
    graph = [[] for _ in range(v+1)]
    visit = [0]*(v+1)
    for _ in range(e):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    num = 1
    def sol(a):
        global num
        q = deque()
        q.append(a)
        visit[a] = 1
        
        while q:
            x = q.popleft()
            for i in graph[x]:
                if visit[i] == 0:
                    q.append(i)
                    if visit[x] == 1:
                        visit[i] = 2
                    elif visit[x] == 2:
                        visit[i] = 1
                elif visit[x] == visit[i]:
                    num = 0
                    
    for i in range(1,v+1):
        if visit[i] == 0:
            sol(i)
    if num:
        print("YES")
    else:
        print("NO")
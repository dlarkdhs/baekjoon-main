import sys
input = sys.stdin.readline
from collections import deque

t = int(input())

for _ in range(t):
    a,b = map(int,input().split())
    
    visit = [False for _ in range(10001)]
    q = deque()
    q.append([a,''])
    visit[a] = True
    
    while q:
        n,m = q.popleft()
        if n == b:
            print(m)
            break
        d = n * 2 % 10000
        if not visit[d]:
            visit[d] = True
            q.append([d,m+'D'])
        s = (n-1) % 10000
        if not visit[s]:
            visit[s] = True
            q.append([s,m+'S'])
        l = n // 1000 + (n % 1000) * 10
        if not visit[l]:
            visit[l] = True
            q.append([l,m+'L'])
        r = n // 10 + (n % 10) * 1000
        if not visit[r]:
            visit[r] = True
            q.append([r,m+'R'])
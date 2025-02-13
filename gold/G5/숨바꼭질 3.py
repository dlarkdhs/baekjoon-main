import sys
input = sys.stdin.readline
from collections import deque

n,k = map(int,input().split())
lim = 100001
t = [0]*lim

def bfs(x,y):
    q = deque()
    if x == 0:
        q.append(1)
    else:
        q.append(x)
    
    while q:
        x = q.popleft()
        if y == x:
            return t[x]
        for i in (x-1,x+1,2*x):
            if 0 <= i < lim and t[i] == 0:
                if i == 2*x:
                    t[i] = t[x]
                    q.appendleft(i)
                else:
                    t[i] = t[x]+1
                    q.append(i)
if n == 0:
    if k == 0:
        print(0)
    else:
        print(bfs(n,k)+1)
else:
    print(bfs(n,k))
import sys
input = sys.stdin.readline
from collections import deque

def dfs(x,y):
   q = deque()
   building[x] = 1
   q.append(x)
   
   while q:
       x = q.popleft()
       for i in (x+u,x-d):
           if 0 <= i < f and building[i] == 0:
               q.append(i)
               building[i] = building[x]+1

f,s,g,u,d = map(int,input().split())
building = [0]*(f+1)
dfs(s-1,g-1)
if building[g-1] == 0:
    print('use the stairs')
else:
    print(building[g-1]-1)
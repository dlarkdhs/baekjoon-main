import sys
from collections import deque
input = sys.stdin.readline

def bfs(n,k):
    time = [0]*200001
    q = deque([n])
    time[n] = 0
    
    while q:
        now = q.popleft()
        if now == k:
            print(time[k])
            return
        if abs(k-now) > abs(k-2*now) and time[2*now] == 0:
            q.append(2*now)
            time[2*now] = time[now]+1
        if now+1 < 100000 and time[now+1] == 0:
            q.append(now+1)
            time[now+1] = time[now]+1
        if now-1 >= 0 and time[now-1] == 0:
            q.append(now-1)
            time[now-1] = time[now]+1

n,m = map(int,input().split())
bfs(n,m)
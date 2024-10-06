import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
que = deque(range(1,n+1))
idx = list(map(int,input().split()))
cnt = 0
for i in idx:
    while True:
        if que.index(i) <= len(que) // 2:
            if i == que[0]:
                que.popleft()
                break
            else:
                cnt += 1
                que.rotate(-1)
        else:
            if i == que[0]:
                que.pop()
                break
            else:
                cnt += 1
                que.rotate(1)
print(cnt)
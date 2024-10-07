import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
for i in range(N):
    n,m = map(int,input().split())
    ip = deque(map(int,input().split()))
    cnt = 0
    while ip:
        big = max(ip)
        front = ip.popleft()
        m -= 1
        if big == front:
            cnt += 1
            if m < 0:
                print(cnt)
                break
        else:
            ip.append(front)
            if m < 0:
                m = len(ip)-1
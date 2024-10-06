import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
balloon = deque(enumerate(map(int,input().split())))
ans = []

while balloon:
    idx, paper = balloon.popleft()
    ans.append(idx+1)
    if paper > 0:
        balloon.rotate(-(paper-1))
    elif paper < 0:
        balloon.rotate(-paper)
        
print(' '.join(map(str,ans)))
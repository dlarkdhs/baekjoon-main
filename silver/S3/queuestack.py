import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
m = int(input())
c = map(int,input().split())
newque = deque()
res = []
for i in range(n):
    if a[i] == 0:
        newque.append(b[i])
for i in c:
    newque.appendleft(i)
    res.append(newque[-1])
    newque.pop()
print(*res, sep = ' ')
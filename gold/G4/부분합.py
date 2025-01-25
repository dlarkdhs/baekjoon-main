import sys
input = sys.stdin.readline

n,s = map(int,input().split())
a = list(map(int,input().split()))

res = 0
d = sys.maxsize
start,end = 0,0

while True:
    if res >= s:
        d = min(d,end-start)
        res -= a[start]
        start += 1
    elif end == n:
        break
    else:
        res += a[end]
        end += 1
if d == sys.maxsize:
    print(0)
else:
    print(d)
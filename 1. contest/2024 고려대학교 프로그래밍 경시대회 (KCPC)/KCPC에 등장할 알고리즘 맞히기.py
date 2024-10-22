import sys
input = sys.stdin.readline

n = int(input())
d = {}
for i in range(n):
    a = []
    a.append(input().split())
    for i in range(2,int(a[0][1])+2):
        if a[0][i] not in d:
            d[a[0][i]] = 1
        else:
            d[a[0][i]] += 1
res = []
for i in d.values():
    res.append(i)
NUM = max(res)
a = [k for k,v in d.items() if v == NUM]
if len(a) == 1:
    print(*a)
else:
    print(-1)
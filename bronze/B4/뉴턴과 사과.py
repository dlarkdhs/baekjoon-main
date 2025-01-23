import sys
input = sys.stdin.readline

p = list(map(int,input().split()))
x,y,r = map(int,input().split())

res = []
for i in p:
    if i == x:
        res.append(p.index(i)+1)

if len(res) == 0:
    print(0)
else:
    print(*res)
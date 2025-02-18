import sys
input = sys.stdin.readline

n,h = map(int,input().split())
u = [0]*(h+1)
d = [0]*(h+1)

for i in range(n):
    a = int(input())
    if i % 2 == 0:
        d[a] += 1
    else:
        u[a] += 1

for i in range(h-1,0,-1):
    u[i] += u[i+1]
    d[i] += d[i+1]

cnt = 0
m = n
for i in range(1,h+1):
    tmp = u[h-i+1]+d[i]
    if m == tmp:
        cnt += 1
    if m > tmp:
        m = tmp
        cnt = 1
print(m,cnt)
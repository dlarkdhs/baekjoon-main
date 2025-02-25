import sys
input = sys.stdin.readline

n = int(input())
p = []
m = []

s = 0
for _ in range(n):
    num = int(input())
    if num > 1:
        p.append(num)
    elif num <= 0:
        m.append(num)
    else:
        s += num
p.sort(reverse=True)
m.sort()

for i in range(0,len(p),2):
    if i+1 >= len(p):
        s += p[i]
    else:
        s += (p[i]*p[i+1])
for i in range(0,len(m),2):
    if i+1 >= len(m):
        s += m[i]
    else:
        s += (m[i]*m[i+1])
print(s)
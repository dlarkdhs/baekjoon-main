import sys
input = sys.stdin.readline

n = int(input())

a,b,c,d = map(int,input().split())
x1 = [a]
y1 = [b]
x2 = [c]
y2 = [d]
print(abs(x1[-1]-x2[-1])*2+abs(y1[-1]-y2[-1])*2)

for _ in range(n-1):
    a,b,c,d = map(int,input().split())
    if a < x1[-1]:
        x1.append(a)
    if b < y1[-1]:
        y1.append(b)
    if c > x2[-1]:
        x2.append(c)
    if d > y2[-1]:
        y2.append(d)
    print(abs(x1[-1]-x2[-1])*2+abs(y1[-1]-y2[-1])*2)
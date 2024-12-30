import sys
input = sys.stdin.readline

n = int(input())
d = list(map(int,input().split()))
d = d[::-1]

a,b = 1,1
for i in range(len(d)):
    if i == 0:
        b = d[i]
        continue
    a = d[i] * b + a
    a,b = b,a
print(b-a,b)
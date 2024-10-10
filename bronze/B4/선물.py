import sys
input = sys.stdin.readline

n,x = map(int,input().split())
a = list(map(int,input().split()))
res = []
for i in range(n-1):
    res.append(a[i] + a[i+1])
print(min(res)*x)
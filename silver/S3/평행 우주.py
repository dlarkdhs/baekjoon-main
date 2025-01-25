import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
v = a[-1]

for i in range(n-2,-1,-1):
    if a[i] > v:
        v = a[i]
    else:
        if v % a[i]:
            v = (v//a[i]+1)*a[i]
print(v)
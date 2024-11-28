import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))

res = 2*n
res1 = sum(a)*2
res2 = a[0]+a[-1]

res3 = 0
for i in range(n-1):
    res3 += abs(a[i]-a[i+1])
print(res+res1+res2+res3)
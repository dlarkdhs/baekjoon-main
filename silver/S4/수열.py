import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))

dp1 = [1]*n
dp2 = [1]*n
for i in range(n-1):
    if a[i+1] >= a[i]:
        dp1[i+1] += dp1[i]
for i in range(n-1):
    if a[i+1] <= a[i]:
        dp2[i+1] += dp2[i]
print(max(max(dp1),max(dp2)))